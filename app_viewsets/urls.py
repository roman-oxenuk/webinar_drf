from django.urls import path, include

from app_viewsets import views


user_list = views.PostsViewSet.as_view({'get': 'list'})
user_detail = views.PostsViewSet.as_view({'get': 'retrieve'})


urlpatterns = [
    path('posts/', user_list),
    path('posts/<int:pk>/', user_detail),
]


# Пример для использования роутера
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('posts', views.PostsViewSet, basename='posts')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
