from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    path('contact', views.contact, name='contact')
]