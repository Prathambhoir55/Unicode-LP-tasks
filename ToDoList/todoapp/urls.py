from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoHome, name='Tasks'),
    path('todo-create', views.TodoCreate, name='Create Task'),
    
]