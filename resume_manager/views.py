from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
# Create your views here.

def posts(request):
    return commonRequestHelper(request, Post)


def commonRequestHelper(request, model):
    _model = [model.objects.filter(published_at__isnull=False).order_by('-published_at').first()]
    _serialized = serializers.serialize('json', _model)
    return HttpResponse(_serialized, content_type="text/json-comment-filtered") 
