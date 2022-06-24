import jwt
import requests
from rest_framework import status
from json.decoder import JSONDecodeError

from django.conf import settings
from django.http import JsonResponse

from cores.permissions import CustomReadOnly
from rest_framework import generics
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserProfileSerializer
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

class UserProfile(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[CustomReadOnly]

    def get_queryset(self):
        user = self.request.user.id
        queryset = User.objects.filter(id=user)
        return queryset

# 2번안 이부분은 추가로 리팩토링 필요함
class GoogleLoginView(generics.GenericAPIView):
    # 소셜로그인을 하면 User테이블에 아이디와 패스워드를 담아둔다.
    
    def get(self,request): 
        # id_token만 해서 헤더로 받기
        token    = request.headers["Authorization"] 
        # 프론트엔드에서 HTTP로 들어온 헤더에서 id_token(Authorization)을 변수에 저장
        url      = 'https://oauth2.googleapis.com/tokeninfo?id_token=' 
        # 토큰을 이용해서 회원의 정보를 확인하기 위한 gogle api주소
        response = requests.get(url+token)
        #구글에 id_token을 보내 디코딩 요청
        user     = response.json()
        # 유저의 정보를 json화해서 변수에 저장

        if User.objects.filter(social_login_id = user['sub']).exists():
            #기존에 가입했었는지 확인
            user_info           = User.objects.get(social_login_id=user['sub'])
            # 가입된 데이터를 변수에 저장
            encoded_jwt         = jwt.encode({'id': user["sub"]}, settings.SECRET_KEY, algorithm='HS256')
            # jwt토큰 발행
            none_member_type    = 1

            return JsonResponse({ # 프론트엔드에게 access token과 필요한 데이터 전달
                'access_token'  : encoded_jwt.decode('UTF-8'),
                'user_name'     : user['name'],
                'user_type'     : none_member_type,
                'user_pk'       : user_info.id
            }, status = 200)            
        else:
            new_user_info = User( # 처음으로 소셜로그인을 했을 경우 회원으 정보를 저장(email이 없을 수도 있다 하여, 있으면 저장하고, 없으면 None으로 표기)
                social_login_id = user['sub'],
                name            = user['name'],
                email           = user.get('email', None)
            )
            new_user_info.save() # DB에 저장
            encoded_jwt         = jwt.encode({'id': new_user_info.id}, settings.SECRET_KEY, algorithm='HS256') # jwt토큰 발행
        
            return JsonResponse({ # DB에 저장된 회원의 정보를 access token과 같이 프론트엔드에게 전달
            'access_token'      : encoded_jwt.decode('UTF-8'),
            'user_name'         : new_user_info.name,
            'user_type'         : none_member_type,
            'user_pk'           : new_user_info.id,
            }, status = 200)





#1번안
# state = getattr(settings, 'STATE')

# BASE_URL = 'http://localhost:8000/'
# GOOGLE_CALLBACK_URI = BASE_URL + 'accounts/google/callback/'

# def google_login(request):
#     scope = "https://www.googleapis.com/auth/userinfo.email"
#     client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
#     print(11231231231231231)
#     return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")

# def google_callback(request):
#     client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
#     client_secret = getattr(settings, "SOCIAL_AUTH_GOOGLE_SECRET")
#     code = request.GET.get('code')
#     """
#     Access Token Request
#     """
#     token_req = requests.post(
#         f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}"
#         )
#     token_req_json = token_req.json()
#     error = token_req_json.get("error")

#     if error is not None:
#         raise JSONDecodeError(error)

#     access_token = token_req_json.get('access_token')
#     email_req = requests.get(
#         f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")

#     email_req_status = email_req.status_code
#     if email_req_status != 200:
#         return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

#     email_req_json = email_req.json()
#     email = email_req_json.get('email')
#     """
#     Signup or Signin Request
#     """
#     try:
#         user = User.objects.get(email=email)
        
#         social_user = SocialAccount.objects.get(user=user)
        

#         if social_user is None:
#             return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)

#         if social_user.provider != 'google':
#             return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

#         # 기존에 Google로 가입된 유저
#         data = {'access_token': access_token, 'code': code}

#         accept = requests.post(
#             f"{BASE_URL}accounts/google/login/finish/", data=data)
#         accept_status = accept.status_code

#         if accept_status != 200:
#             return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)

#         accept_json = accept.json()
#         accept_json.pop('user', None)
#         return JsonResponse(accept_json)

#     except User.DoesNotExist:
#         # 기존에 가입된 유저가 없으면 새로 가입
#         data = {'access_token': access_token, 'code': code}
#         accept = requests.post(
#             f"{BASE_URL}accounts/google/login/finish/", data=data)
#         accept_status = accept.status_code
#         if accept_status != 200:
#             return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
#         accept_json = accept.json()
#         accept_json.pop('user', None)
#         return JsonResponse(accept_json)

# class GoogleLogin(SocialLoginView):
#     adapter_class = google_view.GoogleOAuth2Adapter
#     callback_url = GOOGLE_CALLBACK_URI
#     client_class = OAuth2Client