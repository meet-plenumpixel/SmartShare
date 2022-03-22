# from django.shortcuts import render
from django.urls import reverse_lazy
from utils.multi_form_view import MultiFormView
from users.forms import UserRegisterForm, ProfileCreationForm
# Create your views here.


# class HomeTemplateView(TemplateView):
class HomeTemplateView(MultiFormView):
  template_name = 'home/index.html'
  success_url = reverse_lazy('home')

  form_classes = {
    'user_register_form': UserRegisterForm,
    'profile_creation_form': ProfileCreationForm,
  }

  def get(self, request, *args, **kwargs):
    context = self.get_context_data()
    print(f'{context = }')
    return self.render_to_response(context)

  def are_forms_valid(self, forms):
    if super().are_forms_valid(forms):
      user = forms['user_register_form']
      user.save()
      
      profile = forms['profile_creation_form']
      profile.save(commit=False)
      profile.user = user
      profile.save()

      return True
    return False
