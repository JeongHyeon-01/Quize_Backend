import requests

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User,UserRank
from users.serializers import UserProfileSerializer, UserCreateSerialiser
from cores.decorator import login_authorization

class UserCreate(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerialiser

    def get(self,request):
        token    = request.headers["Authorization"]
        url      = 'https://oauth2.googleapis.com/tokeninfo?id_token='
        response = requests.get(url+token)
        user_info     = response.json()
        
        
        #토큰 갱신확인(access : exp 종료시 재발급 및 refresh 까지 만료시 refresh재발급 및 엑세스토큰 발급 )
        if User.objects.filter(uid = user_info['sub']).exists():
            user = User.objects.get(uid = user_info['sub'])
            token = RefreshToken.for_user(user)
            user.refresh = token
            user.save()
            response = Response(status = 200)
            response.set_cookie("access_token", token.access_token, httponly=True)
            response.set_cookie("refresh_token", user.refresh, httponly=True)
            return response

        user = User.objects.create(
            uid = user_info['sub'],
            picture = user_info['picture'],
            username = user_info['name'],
            email = user_info['email'],
        )
        token = RefreshToken.for_user(user)
        user.refresh = token
        UserRank.objects.create(user_id=user.id)
        user.save()
        response = Response(status = 201)
        response.set_cookie("access_token", token.access_token, httponly=True)
        response.set_cookie("refresh_token", user.refresh, httponly=True)
        return response

class UserProfile(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    
    @login_authorization
    def list(self, request):
        user = request.user.id
        queryset = User.objects.filter(id=user)
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)