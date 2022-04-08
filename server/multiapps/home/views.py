# from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from home import forms as home_form


# class HomeTemplateView(TemplateView):

class HomeTemplateView(TemplateView):
  template_name = 'home/index.html'

  
class ExpenseGroupCreateView(LoginRequiredMixin, CreateView):
  form_class = home_form.ExpenseGroupForm
  template_name = 'home/expensegroup_form.html'
  success_url = reverse_lazy('view-gp')

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


class ExpenseGroupListView(LoginRequiredMixin, ListView):
  template_name = 'home/expensegroup_list.html'
  context_object_name = 'groups'
  ordering = ('name',)

  def get_queryset(self):
    user = self.request.user
    # select_related and prefetch_related | Django n+1 Query Problem
    queryset = ( user.my_groups.all() | user.joined_groups.all() ).distinct()
    return queryset



# class UserListView(LoginRequiredMixin, ListView):
#   login_url = reverse_lazy('login')
#   permission_denied_message = 'first login'

#   model = user_model.User
#   template_name = 'user/user_list.html'
#   context_object_name = 'users_profile'
#   # ordering = ['user']
#   paginate_by = 1

#   def get(self, request, *args, **kwargs):
#     if (paginate_by:=request.GET.get('paginate_by', None)):
#       self.paginate_by = paginate_by
#     self.extra_context = {'paginate_by':self.paginate_by}

#     return super().get(request, *args, **kwargs)

