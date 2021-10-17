from django.contrib.auth.hashers import make_password
from django.db import connections
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib import auth

import dsuser
from dsuser.models import Dsuser
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = Dsuser(
            userId=form.data.get('userId'),
            email=form.data.get('email'),
            password=make_password( form.data.get('password'))
        )

        user.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self,form):
        userId = form.cleaned_data.get("userId")
        password = form.cleaned_data.get("password")
        dsuser = authenticate(self.request, username=userId, password=password)
        
        if dsuser is not None:
            self.request.session['user'] = userId
            login(self.request, dsuser)

        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/user/login')
    
