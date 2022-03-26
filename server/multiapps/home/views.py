# from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, ListView
from utils.multi_form_view import MultiFormView

from account import forms as user_form
from account import models as user_model

# Create your views here.


# class HomeTemplateView(TemplateView):
class HomeTemplateView(MultiFormView):
  template_name = 'home/index.html'
  success_url = reverse_lazy('home')





class UserUpdateView(UpdateView):
  model = user_model.UserAccount
  form_class = user_form.UserUpdateForm
  template_name = 'user/user_detail.html'
  success_url = reverse_lazy('profile_detail')
  

  def get_object(self, *args, **kwargs):
    self.kwargs[self.pk_url_kwarg] = self.request.user.pk
    # print(self.kwargs)
    return super().get_object(*args, **kwargs)


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

