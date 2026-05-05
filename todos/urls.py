from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.todo_list, name='todo-list'),
    path('create/', views.todo_create, name='todo-create'),
    path('toggle/<int:pk>/', views.todo_toggle, name='todo-toggle'),
    path('delete/<int:pk>/', views.todo_delete, name='todo-delete'),
]