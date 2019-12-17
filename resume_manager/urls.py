from django.urls import path
from . import views

urlpatterns = [
    path('api/aboutme', views.aboutme, name='aboutme'),
    path('api/career', views.career, name='career'),
    path('api/education', views.education, name='education'),
    path('api/skill', views.skill, name='skill'),
    path('api/project', views.project, name='project'),
]