from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .form import TaskForm
from .models import Tareas
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password2'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'login.html', {
                    'form': UserCreationForm,
                    'error': 'username already exists'
                })


@login_required
def tareas(request):
    tareas = Tareas.objects.filter(user=request.user)
    return render(request, 'tareas.html', {
        'tareas': Tareas.objects.filter(user=request.user)
    })


@login_required
def tareas_completed(request):
    tareas = Tareas.objects.filter(
        user=request.user).order_by('-datecompleted')
    return render(request, 'tareas.html', {'tareas': tareas})


@login_required
def detail(request, id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tareas, pk=id)
        form = TaskForm(instance=tarea)
        return render(request, 'detail.html', {'tareas': tarea, 'form': form})
    else:
        try:
            tarea = get_object_or_404(Tareas, pk=id, user=request.user)
            form = TaskForm(request.POST, instance=tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detail.html', {'tareas': tarea, 'form': form, 'error': "error updating task"})


@login_required
def complete_tarea(request, id):
    tarea = get_object_or_404(Tareas, pk=id, user=request.user)
    if request.method == 'POST':
        tarea.datecompleted = timezone.now()
        tarea.save()
        return redirect('home')


def delete_tarea(request, id):
    tarea = get_object_or_404(Tareas, pk=id, user=request.user)
    if method == 'POST':
        tarea.delete()
        return redirect('home')


def create_tarea(request):
    if request.method == 'GET':
        return render(request, 'create_tareas.html', {
            'form': TaskForm
        })
    else:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        print(new_task)
        return render(request, 'tareas.html', {
            'form': TaskForm
        })


@login_required
def out(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST
                            ['password'])

    if user is None:
        return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'user o password incorrect'
        })
    else:
        login(request, user)
        return redirect('singnin')
