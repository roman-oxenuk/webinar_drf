import json

from django.core import serializers
from django.views.generic.base import View
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse

from posts_models.models import Post
from app_cbv.forms import PostForm


class PostListView(MultipleObjectMixin, View):

    model = Post

    def get(self, request, *args, **kwargs):
        posts_qs = self.get_queryset()
        return HttpResponse(
            serializers.serialize('json', posts_qs, indent=4),
            content_type='application/json'
        )

    def post(self, request, *args, **kwargs):
        post_data = json.loads(request.body)
        post_form = PostForm(post_data)

        if post_form.is_valid():
            post_form.save()
            return HttpResponse('OK', status=201)

        return HttpResponse(
            json.dumps(post_form.errors),
            content_type='application/json'
        )


class PostDetailView(SingleObjectMixin, View):

    model = Post

    def get(self, request, *args, **kwargs):
        post_obj = self.get_object()
        return HttpResponse(
            serializers.serialize('json', [post_obj], indent=4),
            content_type='application/json'
        )

    def put(self, request, *args, **kwargs):
        post_obj = self.get_object()
        post_data = json.loads(request.body)
        post_form = PostForm(instance=post_obj, data=post_data)

        if post_form.is_valid():
            post_form.save()
            return HttpResponse('OK')

        return HttpResponse(
            json.dumps(post_form.errors),
            content_type='application/json'
        )

    def delete(self, request, *args, **kwargs):
        post_obj = self.get_object()
        post_obj.delete()
        return HttpResponse(status=204)

