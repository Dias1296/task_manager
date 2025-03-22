from django.urls import path
from . import views

urlpatterns = [
  path('', views.task_list, name='task_list'),
  path('create/', views.task_create, name='task_create'),
  path('update/<int:task_id>/', views.task_update, name='task_update'),
  path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
  path('register/', views.register, name='register'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
]