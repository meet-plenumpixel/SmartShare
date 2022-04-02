from django.urls import path
from home import views as home_views


urlpatterns = [
  path('', home_views.HomeTemplateView.as_view(), name='home'),
  path('create-gp/', home_views.ExpenseGroupCreateView.as_view(), name='create-gp'),
  path('view-gp/', home_views.ExpenseGroupListView.as_view(), name='view-gp'),
]
