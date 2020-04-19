import json

from django.core import serializers
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from posts_models.models import Post
from app_plain_views.forms import PostForm


def posts_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return HttpResponse(
            serializers.serialize('json', posts, indent=4),
            content_type='application/json'
        )

    elif request.method == 'POST':
        post_data = json.loads(request.body)
        post_form = PostForm(post_data)

        if post_form.is_valid():
            post_form.save()
            return HttpResponse('OK', status=201)

        return HttpResponse(
            json.dumps(post_form.errors),
            content_type='application/json'
        )

    return HttpResponse(status=405)


def posts_detail(request, pk):
    if request.method == 'GET':
        post_obj = get_object_or_404(Post, pk=pk)
        return HttpResponse(
            serializers.serialize('json', [post_obj], indent=4),
            content_type='application/json'
        )

    elif request.method == 'PUT':
        post_obj = get_object_or_404(Post, pk=pk)
        post_data = json.loads(request.body)
        post_form = PostForm(instance=post_obj, data=post_data)

        if post_form.is_valid():
            post_form.save()
            return HttpResponse('OK')

        return HttpResponse(
            json.dumps(post_form.errors),
            content_type='application/json'
        )

    elif request.method == 'DELETE':
        post_obj = get_object_or_404(Post, pk=pk)
        post_obj.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=405)
