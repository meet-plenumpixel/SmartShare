from django.urls import path
from home import views as home_views
from account import views as user_views


urlpatterns = [
  path('', home_views.HomeTemplateView.as_view(), name='home'),
  path('profile/', home_views.UserUpdateView.as_view(), name='profile_detail'),
  # path('profile-list/', user_views.UserListView.as_view(), name='profile_list'),
]
