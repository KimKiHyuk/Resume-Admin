from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Post
# Create your views here.

def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")
