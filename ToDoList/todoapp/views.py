from django.shortcuts import render, redirect
from . import forms
from . import models
import requests


def TodoHome(request):
    Tasks = models.Task.objects.all()
    checks = models.TaskDone.objects.all()
    print(Tasks)
    return render(request,'TodoHome.html', {'Tasks': Tasks, 'checks': checks})

def TodoCreate(request):
    form = forms.TaskForm()

    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Tasks')
    return render(request, 'TodoCreate.html',{'form': form})
