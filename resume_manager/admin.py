from django.contrib import admin
from .models import (
    AboutMe, Career, Education, Skill, Project
)
# Register your models here.

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']