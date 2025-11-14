from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
      model = Task
      exclude = ['user']

      widgets = {
         'due_date' : forms.DateInput(attrs = {'type':'date'}),
         'due_time' : forms.TimeField(attrs = {'type':'time'})
      }

class CreateUser(UserCreationForm):
   class Meta:
      model = User
      fields