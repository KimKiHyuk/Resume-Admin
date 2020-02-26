from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class AboutMe(models.Model):
    name = models.CharField(max_length = 30)
    greet = models.TextField()
    job = models.CharField(max_length = 20)
    profile_image = models.URLField()
    introduce = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '자기소개'

    def __str__(self):
        return self.name

class Career(models.Model):
    company = models.CharField(max_length=20)
    experience = models.TextField()
    position = models.CharField(max_length=20)
    period_start = models.DateField()
    period_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '커리어'

    def __str__(self):
        return self.company

class Education(models.Model):
    insititute = models.CharField(max_length=40)
    type = models.CharField(max_length=20)
    period_start = models.DateField()
    period_end = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '교육기관'

    def __str__(self):
        return self.insititute

class Skill(models.Model):
    name = models.CharField(max_length=20)
    image = models.URLField()
    proficiency = models.IntegerField()
    hasgTags = ArrayField(
        models.CharField(max_length=15)
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '기술스택'

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    subtitie = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    github = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '프로젝트'

    def __str__(self):
        return self.title
