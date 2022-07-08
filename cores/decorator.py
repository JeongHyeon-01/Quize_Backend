import jwt

from django.conf import settings

from rest_framework                       import status
from rest_framework.response              import Response
from rest_framework_simplejwt.exceptions  import TokenError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from users.models import User


def login_authorization(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('access', None)
            payload      = jwt.decode(access_token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT['ALGORITHM'])
            
            user = User.objects.get(id = payload['user_id'])
            
            response = Response(
                            user,
                            status=status.HTTP_200_OK
                        )
            request.user = user

        #토큰 만료시 갱신
        except jwt.exceptions.ExpiredSignatureError:
            try:
                serializer = TokenRefreshSerializer(data={'refresh': request.headers.get('refresh', None)})
                
                if serializer.is_valid(raise_exception=True):
                    access_token  = serializer.validated_data['access']
                    refresh_token = request.headers.get('refresh', None)
                    response      = Response({
                                        "jwt_token": {
                                                        "access": str(access_token),
                                                        "refresh": str(refresh_token),
                                                    },
                                                },
                                            status = 200
                                        )
                    return response
        
            except TokenError: # refresh 토큰까지 만료 시
                return Response({"message": "로그인이 만료되었습니다."},status=status.HTTP_400_BAD_REQUEST)

            except jwt.exceptions.InvalidTokenError: # 토큰 invalid 인 모든 경우
                return Response({"message": "로그인이 만료되었습니다."}, status=status.HTTP_401_UNAUTHORIZED)
                
        except jwt.exceptions.DecodeError:
            return Response({"message" : "jwt.exceptions.DecodeError: Invalid token type. Token must be a <class 'bytes'>"})

        return func(self, request, *args, **kwargs)
    return wrapper