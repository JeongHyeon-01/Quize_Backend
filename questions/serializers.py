import random

from rest_framework import serializers

from questions.models import Answer, Category, Question


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Category
        exclude = ['description']


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Category
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, object):
        try:
            question_list = list(Question.objects.filter(category=object.id))
            
            data  = [{
                        'question': question.content,
                        'image'   : question.image,
                        'answer'  : [{
                                        "answer"        : answer.correct,
                                        "answer_content": answer.content
                                    } for answer in random.sample(list(Answer.objects.filter(question=question)), 5)]
                    } for question in random.sample(question_list, 10)]

            return data
        except ValueError:
            raise serializers.ValidationError("try again")

    class Meta:
        model  = Category
        fields = ['id', 'content']