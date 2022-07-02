from django.db import models
from cores.timestamp import TimeStamp
from users.models import User


class Support(TimeStamp):
    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title        = models.CharField(max_length=200)
    description  = models.TextField()
    confirmation = models.BooleanField(default=False)

    class Meta:
        db_table = 'supports'
