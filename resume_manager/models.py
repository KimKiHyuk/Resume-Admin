from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length = 20)
    content = models.TextField()

class AboutMe(models.Model):
    name = models.CharField(max_length = 30)
    number = models.IntegerField()

class Career(models.Model):
    name = models.CharField(max_length = 40)
    number = models.IntegerField();