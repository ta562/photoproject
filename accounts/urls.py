# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:22:51 2024

@author: Htomo
"""
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name ='accounts'

urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('signup_success/',views.SignUpSuccessView.as_view(),name='signup_success'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('createdeletestudents/',views.CreateDeleteStudentsView.as_view(),name='createdeletestudents'),
     path('api/userlist/get/', views.ajax_get_userlist, name='ajax_get_userlist'),
    ]