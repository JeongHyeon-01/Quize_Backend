import requests

from django.conf import settings
from django.shortcuts       import redirect

from rest_framework          import generics, status
from rest_framework.response import Response

from cores.user_check  import kakao_checked_user,google_checked_user
from cores.decorator   import login_authorization

from users.google      import google_get_access_token, google_get_user_info
from users.kakao       import KakaoAPI

from users.models      import User, UserRank
from users.serializers import UserProfileSerializer, UserCreateSerializer, UserRankSerializer


#만약을 대비한 카카오 로그인
class KakaoLogin(generics.GenericAPIView):
    def get(self, request):
        try:
            acces_token = request.headers.get('Authorization')
            kakao_user  = KakaoAPI(acces_token).kakao_user()

            if kakao_user.get('code') == -401: 
                return Response({'message' : 'Invalid token'}, status=401)

            return Response(kakao_checked_user(kakao_user))
            
        except KeyError: 
            return Response({'message' : 'Key error'}, status=400)    
  
# 원빈님 팀 꺼 참조 백엔드에서 google 로그인 처리
class GoogleUserlogin(generics.GenericAPIView):
    def get(self,request):
        app_key = settings.GOOGLE_OAUTH2_CLIENT_ID
        scope   = "https://www.googleapis.com/auth/userinfo.email " + \
                "https://www.googleapis.com/auth/userinfo.profile"
        
        redirect_uri    = settings.GOOGLE_OAUTH2_REDIRECT_URI
        google_auth_api = 'https://accounts.google.com/o/oauth2/auth'
        
        response = redirect(f'{google_auth_api}?client_id={app_key}&response_type=code&redirect_uri={redirect_uri}&scope={scope}')
        return response

class GoogleUserCreate(generics.GenericAPIView):
    def get(self, request):
        auth_code        = request.GET.get('code')
        google_token_api = "https://oauth2.googleapis.com/token"
        
        access_token = google_get_access_token(google_token_api, auth_code)
        user_data    = google_get_user_info(access_token)
        
        return Response(google_checked_user(user_data), status=status.HTTP_201_CREATED)


#기존 (현재 EC2에서 돌아가는 코드)
class UserCreate(generics.GenericAPIView):
    queryset         = User.objects.all()
    serializer_class = UserCreateSerializer

    def get(self,request):
        try:
            token     =  request.headers["Authorization"]
            url       = 'https://oauth2.googleapis.com/tokeninfo?id_token='
            response  = requests.get(url+token)
            user_info = response.json()
            return Response(google_checked_user(user_info))
        except KeyError:
            return Response({"Error":"Key Error"}, status=400)

class UserProfile(generics.ListAPIView):
    queryset         = User.objects.all()
    serializer_class = UserProfileSerializer
    
    @login_authorization
    def list(self, request):
        user       = request.user.id
        queryset   = User.objects.filter(id=user)
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRankView(generics.ListCreateAPIView):
    @login_authorization
    def create(self, request):
        serializer = UserRankSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user.id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors)

    @login_authorization
    def list(self, request):
        user       = request.user.id
        user_rank  = UserRank.objects.get(user=user)
        serializer = UserRankSerializer(user_rank)
        return Response(serializer.data)