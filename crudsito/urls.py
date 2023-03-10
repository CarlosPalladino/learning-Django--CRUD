"""crudsito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.register, name='login'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/completed/', views.tareas_completed, name='tareas_completed'),
    path('tareas/create/', views.create_tarea, name='create_tareas'),
    path('tareas/<int:id>/', views.detail, name='tareas_detail'),
    path('tareas/<int:id>/complete', views.complete_tarea, name='complete_tarea'),
    path('tareas/<int:id>/delete', views.delete_tarea, name='delete_tarea'),
    path('logout/', views.out, name='logout'),
    path('signin/', views.signin, name='signin'),

]
