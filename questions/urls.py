from django.urls import path

from questions.views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('<int:pk>/category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]