# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView, ListView
from users import models as user_model
from users import forms as user_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.





# class UserDetailView(DetailView):
#   model = user_model.ProfileModel
#   template_name = 'users/user_detail.html'
#   context_object_name = 'profile'

#   def get(self, request, *args, **kwargs):
#     self.kwargs[self.pk_url_kwarg] = self.request.user.profilemodel.pk
#     print(self.kwargs[self.pk_url_kwarg])
#     return super().get(request, *args, **kwargs)


# class UserListView(LoginRequiredMixin, ListView):
#   login_url = reverse_lazy('login')
#   permission_denied_message = 'first login'

#   model = user_model.ProfileModel
#   template_name = 'users/user_list.html'
#   context_object_name = 'users_profile'
#   # ordering = ['user']
#   paginate_by = 1

#   def get(self, request, *args, **kwargs):
#     if (paginate_by:=request.GET.get('paginate_by', None)):
#       self.paginate_by = paginate_by
#     self.extra_context = {'paginate_by':self.paginate_by}

#     return super().get(request, *args, **kwargs)




class UserLoginView(LoginView):
  template_name = 'authentication/login.html'
  next_page = reverse_lazy('home')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

class UserLogoutView(LogoutView):
  template_name = 'authentication/logout.html'


class UserRegisterView(CreateView):
  form_class = user_form.UserRegisterForm
  template_name = 'authentication/register.html'
  success_url = reverse_lazy('home')
