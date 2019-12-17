from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length = 20, null = True)
    content = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)

class AboutMe(models.Model):
    name = models.CharField(max_length = 30)
    greet = models.TextField()
    job = models.CharField(max_length = 20)
    profile_image = models.ImageField()
    introduce = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Career(models.Model):
    company = models.CharField(max_length=20, null = True)
    experience = models.TextField()
    position = models.CharField(max_length=20)
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null = True)

class Education(models.Model):
    insititute = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null = True)

class Skill(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    proficiency = models.IntegerField()
    hasgTags = ArrayField(
        models.CharField(max_length=10)
    )
    created_at = models.DateTimeField(auto_now_add=True, null = True)

class Project(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    subtitie = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    github = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null = True)

def Models():
    return [Post, AboutMe, Career, Education, Skill, Project]
