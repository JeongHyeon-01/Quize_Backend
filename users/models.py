from django.db import models

from cores.timestamp import TimeStamp
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class UserRank(TimeStamp):
    # correct answer는 총 정답 개수를 의미
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    correct_answer = models.IntegerField()
    total_time     = models.IntegerField()
    quiz_passed    = models.IntegerField()
    attempt        = models.IntegerField()

    class Meta:
        db_table = 'user_rank'