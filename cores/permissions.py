import jwt

from django.conf import settings

from rest_framework import permissions

from users.models import User


class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        access_token = request.headers.get('access', None)
        payload      = jwt.decode(access_token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT['ALGORITHM'])
        user         = User.objects.get(id = payload['user_id'])
        
        return obj.user == user or user.is_staff