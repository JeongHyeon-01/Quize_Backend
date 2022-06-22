from rest_framework import serializers

from questions.models  import Category
from users.models      import UserRank


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Category
        exclude = ['description']


class CategoryDetailSerializer(serializers.ModelSerializer):
    attempt = serializers.SerializerMethodField()

    def get_attempt(self, object):
        user    = self.context['request'].user
        attempt = UserRank.objects.filter(user=user)
        return attempt

    class Meta:
        model  = Category
        fields = '__all__'