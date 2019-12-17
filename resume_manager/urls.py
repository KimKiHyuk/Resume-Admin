from django.urls import path
from . import views

urlpatterns = [
    path('api/aboutme/last', views.aboutme, name='aboutme'),
    path('api/career/last', views.career, name='career'),
    path('api/education/last', views.education, name='education'),
    path('api/skill/last', views.skill, name='skill'),
    path('api/project/last', views.project, name='project'),
]