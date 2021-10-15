from django.db import connections
from django.shortcuts import render
from django.views.generic.edit import FormView

import dsuser
from dsuser.models import Dsuser
from .forms import RegisterForm, LoginForm


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = Dsuser(
            userId=form.data.get('userId'),
            email=form.data.get('email'),
            password=form.data.get('password')
        )

        user.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
