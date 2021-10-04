from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User



class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=15, widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})))
    first_name = forms.CharField(max_length=15,label='First', widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'})))
    last_name = forms.CharField(max_length=15, label='Last Name', widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'})))
    password1 = forms.CharField(max_length=20, label="Password", widget=(
        forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})))
    password2 = forms.CharField(max_length=20, label="Confirm-Password", widget=(
        forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'})))
    email = forms.CharField(max_length=100,label='Email',widget=(
        forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username', 'password1', 'password2']

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class EditProfileForm(UserChangeForm):

    first_name = forms.CharField(max_length=15,label='First', widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'})))
    last_name = forms.CharField(max_length=15, label='Last Name', widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'})))
    email = forms.CharField(max_length=100,label='Email',widget=(
        forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))

    class Meta:
        model = User
        fields = ['first_name','last_name','email']
