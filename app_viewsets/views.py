from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from posts_models.models import Post
from app_viewsets.serializers import PostSerializer


class PostsViewSet(viewsets.ViewSet):

    def list(self, request):
        posts_qs = Post.objects.all()
        serializer = PostSerializer(posts_qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post_obj = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post_obj)
        return Response(serializer.data)


# Пример применения ModelViewSet
# С ним нам нужно написать меньше кода в сравнении с ViewSet
# class PostsViewSet(viewsets.ModelViewSet):

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
