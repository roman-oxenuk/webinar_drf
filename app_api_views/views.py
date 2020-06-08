import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from posts_models.models import Post
from app_api_views.serializers import PostSerializer


# Можно это раскомментировать, чтобы посмотреть, как меняется объект posts_list
# @api_view(['GET', 'POST'])
def posts_list(request):
    if request.method == 'GET':
        posts_qs = Post.objects.all()
        serializer = PostSerializer(posts_qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        post_data = json.loads(request.body)
        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(status=405)


class PostsDetailApiView(APIView):

    def get(self, request, pk):
        post_obj = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        post_obj = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post_obj = get_object_or_404(Post, pk=pk)
        post_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
