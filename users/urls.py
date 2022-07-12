from django.urls import path

from users.views import UserProfile, UserCreate, UserRankView,GoogleUserlogin,GoogleUserCreate, KakaoLogin
urlpatterns = [
    path('kakao/login/', KakaoLogin.as_view(),name='kakao_login'), # 혹시모를 카카오 로그인
    path('google/', GoogleUserlogin.as_view(), name='google_redirect'), #원빈님 팀 에서 사용하듯이 한다면 살릴걸
    path('google/callback/', GoogleUserCreate.as_view(), name = 'google_user'), #원빈님 팀 에서 사용하듯이 한다면 살릴걸
    path('login/', UserCreate.as_view(), name='user_create'), # 현재 메인
    path('profile/', UserProfile.as_view(), name = 'user_profile'),
    path('rank/', UserRankView.as_view(), name = 'user-rank'),
] 