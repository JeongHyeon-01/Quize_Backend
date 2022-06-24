from users import views
from django.urls import path,include

from users.views import UserProfile,GoogleLoginView

urlpatterns = [
    # path('google/login/', views.google_login, name='google_login'),
    # path('google/callback/', views.google_callback, name='google_callback'),  
    # path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
    path('login/google',GoogleLoginView.as_view()),
    path('profile/', UserProfile.as_view())
] 




