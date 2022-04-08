# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView
from extra_views import UpdateWithInlinesView

from account import forms as user_form
from account import models as user_model
from account.inlines.inline_view import UserGroupInlineFormSet

# Create your views here.


class LoanHistoryUpateView(LoginRequiredMixin, UpdateView):
  # model = user_model.LoanHistory
  form_class = user_form.LoanHistoryForm
  template_name = 'user/loanhistoryform.html'
  success_url = reverse_lazy('repay')

  def get_initial(self):
    initial = super().get_initial()
    initial['have_to_pay'] = None
    return initial

  def get_object(self, *args, **kwargs):
    return self.request.user.borrowed_transactions.get()


class UserGroupCreateView(LoginRequiredMixin, CreateView):
  form_class = user_form.UserGroupForm
  template_name = 'user/usergroup_form.html'
  success_url = reverse_lazy('list_group')

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['members'].queryset = form.fields['members'].queryset.exclude(id=self.request.user.pk)
    if self.request.method not in ("POST", "PUT"):
      del form.fields['owner']
    return form

  def get_initial(self):
    initial = super().get_initial()
    initial['owner'] = self.request.user
    return initial


class UserGroupListView(LoginRequiredMixin, ListView):
  template_name = 'user/usergroup_list.html'
  context_object_name = 'groups'
  ordering = ('name',)

  def get_queryset(self):
    user = self.request.user
    # select_related and prefetch_related | Django n+1 Query Problem
    queryset = ( user.my_groups.all() | user.joined_groups.all() ).distinct()
    return queryset


class UserUpdateView(UpdateWithInlinesView):
  model = user_model.User
  form_class = user_form.UserUpdateForm
  inlines = [UserGroupInlineFormSet]
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
