from users.models import User
from users.models import User, UserRank

from rest_framework import serializers


class UserCreateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("uid","username","picture","email")


class RankprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRank
        fields = ("correct_answer","total_time","quiz_passed","attempt")


class UserProfileSerializer(serializers.ModelSerializer):
    rank_set = RankprofileSerializer(many=True, source='users')

    class Meta:
        model = User
        fields = ("id","uid","username","email","picture","last_login",'rank_set')


class UserRankSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user           = validated_data.get('user')
        correct_answer = validated_data.get('correct_answer')
        total_time     = validated_data.get('total_time')
        quiz_passed    = validated_data.get('quiz_passed')
        attempt        = validated_data.get('attempt')

        rank, is_create = UserRank.objects.get_or_create(
                                        user     = user,
                                        defaults = {
                                            'correct_answer': correct_answer,
                                            'total_time'    : total_time,
                                            'quiz_passed'   : quiz_passed,
                                            'attempt'       : attempt
                                        }
                                    )
        
        if not is_create:
            rank.correct_answer += correct_answer
            rank.total_time     += total_time
            rank.quiz_passed    += quiz_passed
            rank.attempt        += attempt
            rank.save()

        return rank

    class Meta:
        model = UserRank
        fields = ['correct_answer', 'total_time', 'quiz_passed', 'attempt']