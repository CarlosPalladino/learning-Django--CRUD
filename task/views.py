from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
#Create your views here.

def home(request):
    return render(request,'home.html') 

def login(request):
      if request.method == 'GET':
       return render(request,'login.html',{
          'form': UserCreationForm
          })
      else:
          if request.POST['password1'] == request.POST['password2']:
               try:
                     user= User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password2'])
                     user.save()
                     login(request, user)
                     return redirect('tareas')   
               except IntegrityError:
                    return render(request,'login.html',{
                         'form': UserCreationForm,
                         'error': 'username already exists'         
                              })
def tareas(request):
     return render(request,'tareas.html')