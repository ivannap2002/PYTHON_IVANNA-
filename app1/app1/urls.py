"""
URL configuration for app1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1.views import saludo
from . import views2

urlpatterns = [
    path('saludar/', views2.saludo, name='saludar'),
    path('google/', views2.getGoogle, name='google'),
    path('fibonacci/', views2.getFibonacci, name='fibonacci'),
    path('primos/<int:limit>/', views2.getPrimes, name='primos'),
]