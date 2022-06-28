
from django.urls import path

from users.views import UserProfile, UserCreate, UserRankView

urlpatterns = [
    path('login/', UserCreate.as_view(), name='user_create'),
    path('profile/', UserProfile.as_view(), name = 'user_profile'),
    path('rank/', UserRankView.as_view(), name = 'user-rank'),
] 


