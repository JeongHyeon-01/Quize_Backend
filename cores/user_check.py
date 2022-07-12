from datetime import datetime

from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User,UserRank


def google_checked_user(data):
    if User.objects.filter(uid = data['sub']).exists():
        user            = User.objects.get(uid = data['sub'])
        token           = RefreshToken.for_user(user)
        access_token    = token.access_token
        user.refresh    = token
        user.last_login = datetime.today()
        user.save()

        response = {
                    "jwt_token": {
                                    "access" : str(access_token),
                                    "refresh": str(token),
                                },
                    },
        
        return response

    user = User.objects.create(
        uid        = data['sub'],
        picture    = data['picture'],
        first_name = data['family_name'],
        last_name  = data['given_name'],
        username   = data['name'],
        email      = data['email'],
        last_login = datetime.today()
    )

    token        = RefreshToken.for_user(user)
    user.refresh = token

    UserRank.objects.create(user_id=user.id)
    user.save()

    response = {
                "jwt_token": {
                                "access" : str(token.access_token),
                                "refresh": str(token),
                            },
                }    
    return response


def kakao_checked_user(kakao_user):

    user, state = User.objects.get_or_create(
        uid        = kakao_user['id'],
        username   = kakao_user['properties']['nickname'],
        email      = kakao_user['email'],
        last_login = datetime.today(),
        defaults={
            'picture': kakao_user['kakao_account']['profile'].get('profile_image_url', None),
            'last_login' : datetime.today()
            }
    )
    status = 200 if not state else 201
    if not state:
        user.profile_image = kakao_user['kakao_account']['profile'].get('profile_image_url', None)
        user.last_login =  datetime.today()
        user.save()

    token        = RefreshToken.for_user(user)
    user.refresh = token

    UserRank.objects.create(user_id=user.id)
    user.save()

    response = {
        "jwt_token": {
            "access" : str(token.access_token),
            "refresh": str(token),
            },
        "status" : status
        },
    return response
