import requests

from rest_framework                  import serializers
from rest_framework.response         import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User, UserRank


class UserCreateSerializer(serializers.ModelSerializer):
    def get(self, request):
        token     = request.headers["Authorization"]
        url       = 'https://oauth2.googleapis.com/tokeninfo?id_token='
        response  = requests.get(url+token)
        user_info = response.json()

        if User.objects.filter(uid = user_info['sub']).exists():
            queryset     = User.objects.filter(uid = user_info['sub'])
            user         = User.objects.get(uid = user_info['sub'])
            token        = RefreshToken.for_user(user)

            user.refresh = token
            user.save()

            response = Response({
                                "jwt_token": {
                                                "access" : str(token.access_token),
                                                "refresh": str(token),
                                            },
                                        },
                                status = 200
                            )
            return response

        user = User.objects.create(
                        uid      = user_info['sub'],
                        picture  = user_info['picture'],
                        username = user_info['name'],
                        email    = user_info['email'],
                    )

        queryset     = User.objects.filter(id = user.id)
        token        = RefreshToken.for_user(user)
        user.refresh = token

        UserRank.objects.create(user_id=user.id)
        user.save()

        response = Response({
                        "jwt_token": {
                                        "access": str(token.access_token),
                                        "refresh": str(token),
                                    },
                                },
                            status = 201
                        )
        return response

    class Meta:
        model  = User
        fields = ["uid","username","picture","email"]


class UserRankSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user           = validated_data.get('user')
        correct_answer = validated_data.get('correct_answer')
        total_time     = validated_data.get('total_time')
        quiz_passed    = validated_data.get('quiz_passed')
        attempt        = validated_data.get('attempt')

        rank, is_created = UserRank.objects.get_or_create(
                                        user_id  = user,
                                        defaults = {
                                            'correct_answer': correct_answer,
                                            'total_time'    : total_time,
                                            'quiz_passed'   : quiz_passed,
                                            'attempt'       : attempt
                                        }
                                    )
        
        if not is_created:
            rank.correct_answer += correct_answer
            rank.total_time     += total_time
            rank.quiz_passed    += quiz_passed
            rank.attempt        += attempt
            rank.save()

        return rank

    class Meta:
        model  = UserRank
        fields = ['correct_answer', 'total_time', 'quiz_passed', 'attempt']


class UserProfileSerializer(serializers.ModelSerializer):
    rank_set = UserRankSerializer(many=True, source='users')

    class Meta:
        model  = User
        fields = ["id", "uid", "username", "email", "picture", "last_login", "rank_set"]