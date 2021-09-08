from django.db.models import fields
from django.forms import ModelForm
from .models import Task
from accounts.models import MyUser

class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_time', 'task_desc', 'task_done']

