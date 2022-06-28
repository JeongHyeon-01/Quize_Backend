import requests

from rest_framework                  import generics, status
from rest_framework.response         import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models      import User,UserRank
from users.serializers import UserProfileSerializer, UserCreateSerialiser, UserRankSerializer
from cores.decorator   import login_authorization


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
            response = Response({
                "jwt_token": {
                    "access_token": str(token.access_token),
                    "refresh_token": str(token),
                },
            },
                status = 200
                )
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
        response = Response({
            "jwt_token": {
                        "access_token": str(token.access_token),
                        "refresh_token": str(token),
                    },
                },
            status = 201
        )
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


class UserRankView(generics.ListCreateAPIView):

    @login_authorization
    def create(self, request):
        serializer = UserRankSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user.id)
            return Response(serializer.data)
        return Response(serializer.errors)

    @login_authorization
    def list(self, request):
        user       = request.user.id
        user_rank  = UserRank.objects.get(user=user)
        serializer = UserRankSerializer(user_rank)
        return Response(serializer.data)