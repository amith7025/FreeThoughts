from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.login_check,name='login'),
     path('dashboard',views.dashboard)
]