
from django.urls import path,include

from users.views import UserProfile,UserCreate

urlpatterns = [
    path('login/', UserCreate.as_view(), name='user_create'),
    path('profile/', UserProfile.as_view(), name = 'user_profile')
] 


