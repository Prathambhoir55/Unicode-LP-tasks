from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    task_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True) 
    task_name = models.CharField(max_length=100)
    task_time = models.TimeField()
    task_desc = models.TextField(null=True, blank=True)
    task_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
