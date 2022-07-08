from django.db                  import models
from django.contrib.auth.models import AbstractUser

from cores.timestamp import TimeStamp


class User(AbstractUser):
    uid      = models.CharField(max_length=255)
    provider = models.CharField(max_length=50, default='google')
    picture  = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email    = models.CharField(max_length=250, unique=True)
    refresh  = models.TextField(null=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD  = 'email'

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