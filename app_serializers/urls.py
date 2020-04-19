from django.urls import path, include

from app_serializers.views import PostListView, PostDetailView


urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]

