# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView, ListView
from account import forms as user_form
from account import models as user_model

# Create your views here.




class UserDetailView(DetailView):
  model = user_model.UserAccount
  template_name = 'users/user_detail.html'
  context_object_name = 'profile'


class UserListView(LoginRequiredMixin, ListView):
  login_url = reverse_lazy('login')
  permission_denied_message = 'first login'

  model = user_model.UserAccount
  template_name = 'users/user_list.html'
  context_object_name = 'users_profile'
  # ordering = ['user']
  paginate_by = 1

  def get(self, request, *args, **kwargs):
    if (paginate_by:=request.GET.get('paginate_by', None)):
      self.paginate_by = paginate_by
    self.extra_context = {'paginate_by':self.paginate_by}

    return super().get(request, *args, **kwargs)






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
