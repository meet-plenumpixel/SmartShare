from django.urls import path
from account import views as user_views


urlpatterns = [
  path('profile/', user_views.UserUpdateView.as_view(), name='profile_update'),
  path('register/', user_views.UserRegisterView.as_view(), name='register'),
  path('logout/', user_views.UserLogoutView.as_view(), name='logout'),
  path('login/', user_views.UserLoginView.as_view(), name='login'),
]
