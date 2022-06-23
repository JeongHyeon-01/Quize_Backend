from users.models import User
from users.serializers import UserProfileSerializer

from cores.permissions import CustomReadOnly
from rest_framework import generics

class UserProfile(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[CustomReadOnly]

    def get_queryset(self):
        user = self.request.user.id
        queryset = User.objects.filter(id=user)
        return queryset

