from django.db import models

from cores.timestamp import TimeStamp


class DevelopmentGroup(models.Model):
    name  = models.CharField(max_length=50)
    image = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'development_groups'
    

class Category(TimeStamp):
    development_group = models.ForeignKey('DevelopmentGroup', on_delete=models.PROTECT)
    name              = models.CharField(max_length=50)
    image             = models.CharField(max_length=255, null=True)
    description       = models.TextField(null=True)

    class Meta:
        db_table = 'categories'


class Question(TimeStamp):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    content  = models.TextField()
    image    = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'questions'


class Answer(TimeStamp):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    content  = models.TextField()
    correct  = models.BooleanField(default=False)
    image    = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'answers'