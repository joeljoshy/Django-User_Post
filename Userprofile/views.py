from django.urls import reverse_lazy,reverse
from .forms import RegistrationForm,LoginForm,EditProfileForm
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth import login,logout,authenticate
from django.views import generic
from django.views.generic import ListView,DetailView
from django.http import JsonResponse,HttpResponseRedirect
from django.core import serializers

from django.core.paginator import Paginator

# Create your views here.

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):

        return self.request.user

def create_account(request):
    form = RegistrationForm
    context ={'form':form}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('registered')
            return redirect('login')
        else:
            context={'form':form}
            return render(request,'registration.html',context)

    return render(request,'registration.html',context)

def login_view(request):
    form = LoginForm
    context = {'form':form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print('login success')
                return redirect('listall')
            else:
                print('login failed')
                return render(request, 'login.html', context)
    return render(request,'login.html',context)

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
