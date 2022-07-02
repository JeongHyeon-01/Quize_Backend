from django.urls import path

from supports.views import SupportPublicUser,SupportCustomUser

urlpatterns = [
    path('help/', SupportPublicUser.as_view(), name='suport_user'),
    path('help/<int:pk>/',SupportCustomUser.as_view(), name='supprot_custom')
]