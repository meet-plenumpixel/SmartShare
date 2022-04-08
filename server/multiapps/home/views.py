# from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from home import forms as home_form

# Create your views here.

class HomeTemplateView(TemplateView):
  template_name = 'home/index.html'


class ExpenseCreateView(CreateView):
  form_class = home_form.ExpenseForm
  template_name = 'home/expense_form.html'
  success_url = reverse_lazy('home')

  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['group'].queryset = self.request.user.my_groups
    return form



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

