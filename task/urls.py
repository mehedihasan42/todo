from django.contrib import admin
from django.urls import path,include
from .views import task_list,task_create,task_detail,task_mark_completed,register,user_login,user_logout

urlpatterns = [
  path('task/',task_list,name='task_list'),
  path('create/',task_create,name='task_create'),
  path('details/<int:pk>/',task_detail,name='task_detail'),
  path('completed/<int:pk>/',task_mark_completed,name='task_mark_completed'),
  path('register/',register,name='register'),
  path('login/',user_login,name='user_login'),
  path('logout/',user_logout,name='user_logout'),
]
