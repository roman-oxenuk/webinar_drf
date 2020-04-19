from django.views.generic.base import View
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from posts_models.models import Post
from app_serializers.serializers import PostSerializer


class PostListView(MultipleObjectMixin, View):

    model = Post

    def get(self, request, *args, **kwargs):
        posts_qs = self.get_queryset()
        serializer = PostSerializer(posts_qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


class PostDetailView(SingleObjectMixin, View):

    model = Post

    def get(self, request, *args, **kwargs):
        post_obj = self.get_object()
        serializer = PostSerializer(post_obj)
        return JsonResponse(serializer.data)

    def put(self, request, *args, **kwargs):
        post_obj = self.get_object()
        data = JSONParser().parse(request)
        serializer = PostSerializer(post_obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        post_obj = self.get_object()
        post_obj.delete()
        return HttpResponse(status=204)

