# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from account.forms import UserRegisterForm

# Create your views here.


class UserLoginView(LoginView):
  template_name = 'authentication/auth_form.html'
  next_page = reverse_lazy('home')
  extra_context = {
    'submit_btn':'login',
    'form_change_btn':'register'
  }


class UserLogoutView(LogoutView):
  template_name = 'authentication/logout.html'


class UserRegisterView(CreateView):
  form_class = UserRegisterForm
  template_name = 'authentication/auth_form.html'
  success_url = reverse_lazy('home')
  extra_context = {
    'submit_btn':'register',
    'form_change_btn':'login'
  }
