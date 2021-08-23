from django.forms import ModelForm
from .models import Task, TaskDone

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

