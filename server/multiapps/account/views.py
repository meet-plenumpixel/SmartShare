# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView

from account import forms as user_form
from account import models as user_model

# Create your views here.


class UserUpdateView(UpdateView):
  model = user_model.UserAccount
  form_class = user_form.UserUpdateForm
  template_name = 'user/user_detail.html'
  success_url = reverse_lazy('profile_update')
  
  def get_object(self, *args, **kwargs):
    self.kwargs[self.pk_url_kwarg] = self.request.user.pk
    # print(self.kwargs)
    return super().get_object(*args, **kwargs)


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
  form_class = user_form.UserRegisterForm
  template_name = 'authentication/auth_form.html'
  success_url = reverse_lazy('home')
  extra_context = {
    'submit_btn':'register',
    'form_change_btn':'login'
  }
