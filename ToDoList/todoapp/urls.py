from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoHome, name='Tasks'),
    path('todo-create', views.TodoCreate, name='Create Task'),
    path('todo-update/<int:key>', views.TodoUpdate, name='Update Task'),
    path('todo-delete/<int:key>', views.TodoDelete, name='Delete Task'),    
]