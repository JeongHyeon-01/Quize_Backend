from rest_framework import generics

from questions.models      import Category, DevelopmentGroup, Question, Answer
from questions.serializers import CategoryListSerializer, CategoryDetailSerializer, QuizSerializer


class CategoryListView(generics.ListAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        pk                = self.kwargs['pk']
        development_group = DevelopmentGroup.objects.get(pk=pk)
        category          = Category.objects.filter(development_group=development_group)
        return category
        

class CategoryDetailView(generics.RetrieveAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class QuizMainView(generics.RetrieveAPIView):
    queryset         = Category.objects.all()
    serializer_class = QuizSerializer