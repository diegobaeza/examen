from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    path('', include('pwa.urls')),
    path(r'base_layout',views.base_layout,name='base_layout')

]
