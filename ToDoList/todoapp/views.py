from django.shortcuts import render, redirect
from . import forms
from . import models
import requests


def TodoHome(request):
    Tasks = models.Task.objects.all()
    checks = models.TaskDone.objects.all()
    print(Tasks)
    return render(request,'TodoHome.html', {'Tasks': Tasks, 'checks': checks})

def TodoInput(request):
    name=request.POST.get('taskname')
    time=request.POST.get('tasktime')
    return render(request,'TodoInput.html',{'name': name, 'time': time})
