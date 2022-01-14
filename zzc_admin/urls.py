"""zzc_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from backend import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('index/', views.index),
    path('vx_xxx_login/', views.vx_xxx_login),
    path('vx_xxx_btpr/', views.vx_xxx_btpr),
    path('vx_xxx_insert_tpxx/', views.vx_xxx_insert_tpxx),
    path('upload/', views.upload),
    path('download_result/', views.download_result),
    path('datatables/', views.get_datatables)
]
