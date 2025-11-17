from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

    return render(request,'task_list.html',{
        'conpleted_task':conpleted_task,
        'pendding_task':pendding_task,
        'status_filrer':status_filrer,
        'category_filter':category_filter
    })  

@login_required
def task_create(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'task_create.html',{'form':form})    

@login_required
def task_detail(request,pk):
    task = get_object_or_404(Task,id=pk,user=request.user)
    return render(request,'',{'task':task})

@login_required
def task_mark_completed(request,pk):
    task = get_object_or_404(Task,id=pk,user=request.user)
    task.is_completed = True
    task.save()
    return redirect('task_list')


def register(request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})    


def user_login(request):
   if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request,username=username,password=password)

       if user is not None:
          login(request,user)
          messages.success(request,f"Welcome,{user.username}!")
          return redirect('task_list')
       else:
           messages.error(request,"Invalid username or password")

   return render(request,'login.html')   


def user_logout(request):
    logout(request)
    return redirect('user_login')
