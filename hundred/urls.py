from django.contrib import admin
from django.urls import path
from hundred import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate', views.calculate, name='calculate'),
]
