from django.db import models

from cores.timestamp import TimeStamp

class User(models.Model):
    nickname      = models.CharField(max_length=50)
    email         = models.EmailField()
    profile_image = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'users'


class UserRank(TimeStamp):
    # correct answer는 총 정답 개수를 의미
    user           = models.ForeignKey('User', on_delete=models.CASCADE)
    correct_answer = models.IntegerField()
    total_time     = models.IntegerField()
    quiz_passed    = models.IntegerField()
    attempt        = models.IntegerField()

    class Meta:
        db_table = 'user_rank'