from django.urls import path,include
from .views import hello

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', hello)
] 
