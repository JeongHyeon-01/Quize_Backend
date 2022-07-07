import requests

from rest_framework          import generics, status
from rest_framework.response import Response

from cores.decorator   import login_authorization
from users.models      import User, UserRank
from users.serializers import UserProfileSerializer, UserCreateSerializer, UserRankSerializer
from users.user_check  import checked_user


class UserCreate(generics.GenericAPIView):
    queryset         = User.objects.all()
    serializer_class = UserCreateSerializer

    def get(self,request):
        try:
            token     = request.headers["Authorization"]
            url       = 'https://oauth2.googleapis.com/tokeninfo?id_token='
            response  = requests.get(url+token)
            user_info = response.json()
            return Response(checked_user(user_info))
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