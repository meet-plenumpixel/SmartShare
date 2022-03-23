# from django.shortcuts import render
from django.urls import reverse_lazy
from utils.multi_form_view import MultiFormView
from users.forms import UserRegisterForm
# Create your views here.


# class HomeTemplateView(TemplateView):
class HomeTemplateView(MultiFormView):
  template_name = 'home/index.html'
  success_url = reverse_lazy('home')

  form_classes = {
    'user': UserRegisterForm
  }
