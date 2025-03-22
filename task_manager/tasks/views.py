from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
  tasks = Task.objects.filter(user=request.user) # Show only the logged in users task
  return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.user = request.user
      task.save()
      return redirect('task_list')
  else:
    form = TaskForm()
  return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, task_id):
  task = get_object_or_404(Task, id=task_id, user=request.user) #Ensure user owns task
  if request.method == 'POST':
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('task_list')
  else:
    form = TaskForm(instance=task)
  return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
  task = get_object_or_404(Task, id=task_id, user=request.user)
  if request.method == 'POST':
    task.delete()
    return redirect('task_list')
  return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user) # Log the user in after registration
      return redirect('task_list')
  else:
    form = UserCreationForm()
  return render(request, 'tasks/register.html', {'form': form})
  
def user_login(request):
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('task_list')
  else:
    form = AuthenticationForm()
  return render(request, 'tasks/login.html', {'form': form})
  
def user_logout(request):
  logout(request)
  return redirect('login')