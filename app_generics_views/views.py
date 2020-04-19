from posts_models.models import Post
from app_generics_views.serializers import PostSerializer
from rest_framework import generics


class PostsListGenericApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsDetailGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer