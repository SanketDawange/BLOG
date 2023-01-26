from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('postinfo/<str:title>', views.postinfo, name='postinfo'),
    # path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
