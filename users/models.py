from django.db import models

from cores.timestamp import TimeStamp
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    class Meta:
        db_table = 'user'

class UserRank(TimeStamp):
    # correct answer는 총 정답 개수를 의미
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    correct_answer = models.IntegerField(default=0)
    total_time     = models.IntegerField(default=0)
    quiz_passed    = models.IntegerField(default=0)
    attempt        = models.IntegerField(default=0)

    class Meta:
        db_table = 'user_rank'