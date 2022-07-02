import random

from rest_framework import serializers

from supports.models import Support
from users.models     import User
from users.serializers import UserProfileSerializer


class SupportUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]

class SupportSerializers(serializers.ModelSerializer):
    user = SupportUserSerializers(read_only= True)
    class Meta:
        model   = Support
        fields = ["id","user","title","description","created_at","confirmation"]

class SupprotDetailSerializers(serializers.ModelSerializer):
    user = SupportUserSerializers(read_only= True)
    class Meta:
        model   = Support
        fields = ["id","user","title","description","created_at","confirmation"]