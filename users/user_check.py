import requests, jwt
from datetime import datetime
from django.conf import settings
from rest_framework                  import generics, status
from rest_framework.response         import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models      import User,UserRank


def checked_user(data):
    if User.objects.filter(uid = data['sub']).exists():
        user = User.objects.get(uid = data['sub'])
        token = RefreshToken.for_user(user)
        access_token = token.access_token
        user.refresh = token
        user.last_login = datetime.today()
        user.save()
        response = {
            "jwt_token": {
            "access": str(access_token),
            "refresh": str(token),
            },
        },
        
        return response

    user = User.objects.create(
        uid = data['sub'],
        picture = data['picture'],
        first_name = data['family_name'],
        last_name = data['given_name'],
        username = data['name'],
        email = data['email'],
        last_login = datetime.today()
    )
    token = RefreshToken.for_user(user)
    user.refresh = token
    UserRank.objects.create(user_id=user.id)
    user.save()
    response = {
        "jwt_token": {
                    "access": str(token.access_token),
                    "refresh": str(token),
                },
            },
    return response
