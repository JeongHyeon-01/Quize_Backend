from django.urls import path,include

from users.views import UserProfile

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', UserProfile.as_view())
] 




