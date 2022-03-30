# from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, ListView
from django.views.generic.edit import CreateView
from utils.multi_form_view import MultiFormView

from home import forms as home_form
from home import models as home_model


# class HomeTemplateView(TemplateView):
class HomeTemplateView(MultiFormView):
  template_name = 'home/index.html'
  success_url = reverse_lazy('home')
  
  
class ExpenseGroupCreateView(LoginRequiredMixin, CreateView):
  form_class = home_form.ExpenseGroupForm
  template_name = 'home/create_gp.html'
  success_url = reverse_lazy('view-gp')

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs.update({
      'user': self.request.user
    })
    return kwargs
  
  
class ExpenseGroupListView(LoginRequiredMixin, ListView):
  login_url = reverse_lazy('login')
  permission_denied_message = 'first login'


  model = home_model.ExpenseGroup
  context_object_name = 'groups'
  template_name = 'home/view_gp.html'
  ordering = ('id',)

  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      print(context)
      return context
  






# class UserListView(LoginRequiredMixin, ListView):
#   login_url = reverse_lazy('login')
#   permission_denied_message = 'first login'

#   model = user_model.UserAccount
#   template_name = 'users/user_list.html'
#   context_object_name = 'users_profile'
#   # ordering = ['user']
#   paginate_by = 1

#   def get(self, request, *args, **kwargs):
#     if (paginate_by:=request.GET.get('paginate_by', None)):
#       self.paginate_by = paginate_by
#     self.extra_context = {'paginate_by':self.paginate_by}

#     return super().get(request, *args, **kwargs)

