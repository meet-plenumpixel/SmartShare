# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from extra_views import UpdateWithInlinesView

from account import forms as user_form
from account import models as user_model
from home.inlines.inline_view import ExpenseGroupInlineFormSet

# Create your views here.

class UserUpdateView(UpdateWithInlinesView):
  model = user_model.User
  form_class = user_form.UserUpdateForm
  inlines = [ExpenseGroupInlineFormSet]
  template_name = 'user/user_detail.html'
  success_url = reverse_lazy('home')
  
  def get_object(self, *args, **kwargs):
    self.kwargs[self.pk_url_kwarg] = self.request.user.pk
    return super().get_object(*args, **kwargs)


class UserLoginView(LoginView):
  template_name = 'auth/auth_form.html'
  next_page = reverse_lazy('home')
  extra_context = {
    'submit_btn':'login',
    'form_change_btn':'register'
  }


class UserLogoutView(LogoutView):
  template_name = 'auth/logout.html'


class UserRegisterView(CreateView):
  form_class = user_form.UserRegisterForm
  template_name = 'auth/auth_form.html'
  success_url = reverse_lazy('profile')
  extra_context = {
    'submit_btn':'register',
    'form_change_btn':'login'
  }
