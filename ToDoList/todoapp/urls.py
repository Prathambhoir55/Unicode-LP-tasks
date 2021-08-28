from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoUser, name='Users'),
    path('task/<str:pk>', views.TodoHome, name='Tasks'),
    path('todo-create', views.TodoCreate, name='Create Task'),
    path('todo-update/<int:key>', views.TodoUpdate, name='Update Task'),
    path('todo-delete/<int:key>', views.TodoDelete, name='Delete Task'),    
]