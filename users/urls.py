from users import views, google

from django.urls import path,include

from users.views import UserProfile,GoogleLogin

urlpatterns = [
    path('google/login/', google.google_login, name='google_login'),
    path('google/callback/', google.google_callback, name='google_callback'),  
    path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
    # path('login/google',GoogleLoginView.as_view()),
    path('profile/', UserProfile.as_view())
] 




