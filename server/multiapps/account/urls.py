from django.urls import path
from account import views as user_views


urlpatterns = [
  path('login/', user_views.UserLoginView.as_view(), name='login'),
  path('logout/', user_views.UserLogoutView.as_view(), name='logout'),
  path('register/', user_views.UserRegisterView.as_view(), name='register'),
]
