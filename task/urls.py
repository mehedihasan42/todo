from django.contrib import admin
from django.urls import path,include
from .views import task_list,task_create,task_detail,register

urlpatterns = [
  path('task/',task_list,name='task_list'),
  path('create/',task_create,name='task_create'),
  path('details/<int:pk>/',task_detail,name='task_detail'),
  path('register/',register,name='register'),
]
