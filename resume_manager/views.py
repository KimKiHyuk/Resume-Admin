from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
# Create your views here.

def posts(request):
    return commonRequestHelper(request, Post)

def aboutme(request):
    return commonRequestHelper(request, AboutMe)

def career(request):
    return commonRequestHelper(request, Career)

def education(request):
    return commonRequestHelper(request, Education)

def project(request):
    return commonRequestHelper(request, Project)

def skill(request):
    return commonRequestHelper(request, Skill)


def commonRequestHelper(request, model):
    _model = model.objects.filter(created_at__isnull=False).order_by('-created_at')
    _serialized = serializers.serialize('json', _model)
    return HttpResponse(_serialized, content_type="text/json-comment-filtered") 
