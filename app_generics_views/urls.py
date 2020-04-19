from django.urls import path, include

from app_generics_views import views


urlpatterns = [
    path('posts/', views.PostsListGenericApiView.as_view()),
    path('posts/<int:pk>/', views.PostsDetailGenericApiView.as_view()),
]