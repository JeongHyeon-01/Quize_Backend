from rest_framework import serializers

from users.models    import User
from supports.models import Support


class SupportUserSerializers(serializers.ModelSerializer):

    class Meta:
        model  = User
        fields = ["id", "username", "email"]

class SupportSerializers(serializers.ModelSerializer):
    user = SupportUserSerializers(read_only = True)

    class Meta:
        model  = Support
        fields = ["id", "user", "title", "description", "created_at", "confirmation"]

class SupportDetailSerializers(serializers.ModelSerializer):
    user = SupportUserSerializers(read_only = True)

    class Meta:
        model  = Support
        fields = ["id", "user", "title", "description", "created_at", "confirmation"]