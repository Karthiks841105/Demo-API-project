"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list',list1),
    path('reg',regi),
    path('register',register),
    path('log',log),
    path('login',login),
    path('index',menu),
    path('new',new),
    path('main',main),
    path('Mail',sendmail),
    path('submit',submit),
    path('csv1',csv1),
    path('csv2',csv2),
    path('logout',logout),
    path('issue',issue),
    path('loc11',loc11),
    path('demoo',demoo),
]
