from rest_framework import generics

from questions.models      import Category
from questions.serializers import CategoryListSerializer, CategoryDetailSerializer


class CategoryListView(generics.ListAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategoryDetailSerializer