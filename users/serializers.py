from users.models import User
from users.models import User, UserRank

from rest_framework import serializers

class RankprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRank
        fields = ("correct_answer","total_time","quiz_passed","attempt")

class UserProfileSerializer(serializers.ModelSerializer):
    rank_set = RankprofileSerializer(many=True, source='users')
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id","rank_set","extra_data","is_active","last_login")
        depth = 1

    def get_extra_data(self, instance):
        if instance.is_superuser is not True:
            extra_data = instance.socialaccount_set.all()[0].extra_data

            return extra_data
    