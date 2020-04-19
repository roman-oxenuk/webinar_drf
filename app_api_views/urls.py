from django.urls import path, include

from app_api_views import views


urlpatterns = [
    path('posts/', views.posts_list),
    path('posts/<int:pk>/', views.PostsDetailApiView.as_view()),
]

