# from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, ListView
from django.views.generic.edit import CreateView
from utils.multi_form_view import MultiFormView

from home import models as home_model


# class HomeTemplateView(TemplateView):
class HomeTemplateView(MultiFormView):
  template_name = 'home/index.html'
  success_url = reverse_lazy('home')
  
  
class ExpenseGroupCreateView(LoginRequiredMixin, CreateView):
  model = home_model.ExpenseGroup
  fields = ('name', 'members')
  template_name = 'home/create_gp.html'
  success_url = reverse_lazy('view-gp')

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['members'].queryset = form.fields['members'].queryset.exclude(id=self.request.user.pk)
    return form

  def form_valid(self, form):
    self.__obj = form.save(commit=False)
    self.__obj.owner = self.request.user
    return super().form_valid(self.__obj)
  
  def get_success_url(self):
    self.object = self.__obj
    return super().get_success_url()



class ExpenseGroupListView(LoginRequiredMixin, ListView):
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

