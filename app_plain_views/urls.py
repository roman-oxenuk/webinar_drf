from django.urls import path, include

from app_plain_views import views


urlpatterns = [
    path('posts/', views.posts_list),
    path('posts/<int:pk>/', views.posts_detail)
]

