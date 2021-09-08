from django.db import models
from accounts.models import MyUser
import datetime

# Create your models here.

class Task(models.Model):
    task_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True) 
    task_name = models.CharField(max_length=100)
    task_time = models.TimeField()
    task_desc = models.TextField(null=True, blank=True)
    task_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

    def timespan(self):
        if self.task_time >= datetime.time(6, 0, 0) and self.task_time < datetime.time(12, 0, 0):
            period = "Morning Task"
        elif self.task_time >= datetime.time(12, 0, 0) and self.task_time < datetime.time(17, 0, 0):
            period = "Afternoon Task"
        elif self.task_time >= datetime.time(17, 0, 0) and self.task_time < datetime.time(20, 0, 0):
            period = "Evening Task"
        elif self.task_time >= datetime.time(20, 0, 0) and self.task_time <= datetime.time(23, 59, 59):
            period = "Night Task"
        elif self.task_time >= datetime.time(0, 0, 0) and self.task_time < datetime.time(6, 0, 0):
            period = "Night Task"
        return period