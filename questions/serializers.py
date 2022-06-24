import random

from rest_framework import serializers

from questions.models import Answer, Category, Question
from users.models     import UserRank


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Category
        exclude = ['description']


class CategoryDetailSerializer(serializers.ModelSerializer):
    attempt = serializers.SerializerMethodField()

    def get_attempt(self, object):
        user    = self.context['request'].user
        attempt = UserRank.objects.filter(user=user)
        return attempt

    class Meta:
        model  = Category
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, object):
        question_list = list(Question.objects.filter(category=object.id))
        
        data  = [{
                    'question': question.content,
                    'image'   : question.image,
                    'asnwer'  : [{
                                    "answer"        : answer.correct,
                                    "answer_content": answer.content
                                } for answer in random.sample(list(Answer.objects.filter(question=question)), 5)]
                } for question in random.sample(question_list, 10)]

        return data

    class Meta:
        model = Category
        fields = ['id', 'content']