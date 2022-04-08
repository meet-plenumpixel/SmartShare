from django.urls import path
from account import views as user_views


urlpatterns = [
  path('repay/', user_views.LoanHistoryUpateView.as_view(), name='repay'),

  path('group/add/', user_views.UserGroupCreateView.as_view(), name='add_group'),
  path('group/view/', user_views.UserGroupListView.as_view(), name='list_group'),
  
  path('profile/', user_views.UserUpdateView.as_view(), name='profile'),
  path('register/', user_views.UserRegisterView.as_view(), name='register'),
  path('logout/', user_views.UserLogoutView.as_view(), name='logout'),
  path('login/', user_views.UserLoginView.as_view(), name='login'),
]
