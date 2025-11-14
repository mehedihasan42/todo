from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def task_list(request):
    status_filrer = request.GET.get('status','all')
    category_filter = request.GET.get('category','all')
    task = Task.objects.filter(user = request.user)

    if status_filrer != 'all':
        task = task.filter(is_completed = (status_filrer == 'completed'))

    if category_filter != 'all':
        task = task.filter(category = category_filter)  

    conpleted_task = task.filter(is_completed = True)    
    pendding_task = task.filter(is_completed = False)

    return render(request,'',{
        'conpleted_task':conpleted_task,
        'pendding_task':pendding_task,
        'status_filrer':status_filrer,
        'category_filter':category_filter
    })  


def task_create(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('')
    else:
        form = TaskForm()
    return render(request,'',{'form':form})    

def task_detail(request,pk):
    task = get_object_or_404(Task,id=pk,user=request.user)
    return render(request,'',{'task':task})


def task_mark_completed(request,pk):
    task = get_object_or_404(Task,id=pk,user=request.user)
    task.is_completed = True
    task.save()
    return redirect('')

def register(request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get(username)
        password = form.cleaned_data.get(password)
        user = authenticate(username,password)
        login(user)
        return redirect('')
    else:
        form = UserCreationForm()
    return render(request,'',{'form':form})    

