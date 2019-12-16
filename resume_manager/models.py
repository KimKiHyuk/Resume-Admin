from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length = 20, null = True)
    content = models.TextField(null = True)
    published_at = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    name = models.CharField(max_length = 30)
    greet = models.TextField(null=True)
    job = models.CharField(max_length = 20, null=True)
    profile_image = models.ImageField(null=True)
    introduce = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)

class Career(models.Model):
    period_from = models.DateField(null = True)

class Models:
    def __init__(self):
        self.modelList = [Post, AboutMe, Career]
