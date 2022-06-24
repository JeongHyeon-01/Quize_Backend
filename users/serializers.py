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


