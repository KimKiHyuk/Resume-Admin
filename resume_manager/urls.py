from django.urls import path
from . import views

urlpatterns = [
    path('api/aboutme/last', views.posts, name='aboutme'),
    path('api/career/last', views.posts, name='career'),
    path('api/education/last', views.posts, name='education'),
    path('api/skill/last', views.posts, name='skill'),
    path('api/project/last', views.posts, name='project'),
]