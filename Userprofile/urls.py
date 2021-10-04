from django.urls import path
from .views import create_account,login_view,UserEditView,signout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('user/register',create_account,name='register'),
    path('home/profile',login_required( lambda request: render(request, 'profile.html'),login_url='login'), name='profile'),
    path('',login_view,name='login'),
    path('user/logout',login_required(signout,login_url='login'),name='logout'),
    path('home',login_required(lambda request:render(request,'base.html'),login_url='login'),name='home'),
    path('edit_profile',login_required(UserEditView.as_view(),login_url='login'),name='edit_profile'),

]