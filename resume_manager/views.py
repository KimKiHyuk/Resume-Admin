from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST'])
def posts(request):
    return commonRequestHelper(request, Post)

@api_view()
def aboutme(request):
    return commonRequestHelper(request, AboutMe)

@api_view()
def career(request):
    return commonRequestHelper(request, Career)

@api_view()
def education(request):
    return commonRequestHelper(request, Education)

@api_view()
def project(request):
    return commonRequestHelper(request, Project)

@api_view()
def skill(request):
    return commonRequestHelper(request, Skill)


def commonRequestHelper(request, model):
    _model = model.objects.filter(created_at__isnull=False).order_by('-created_at')
    _serialized = serializers.serialize('json', _model)
    return HttpResponse(_serialized, content_type="text/json-comment-filtered") 
