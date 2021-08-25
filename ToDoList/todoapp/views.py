from django.shortcuts import render, redirect
from . import forms
from . import models
import requests


def TodoHome(request):
    Tasks = models.Task.objects.all()
    return render(request,'TodoHome.html', {'Tasks': Tasks})

def TodoCreate(request):
    form = forms.TaskForm()

    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Tasks')
    return render(request, 'TodoCreate.html',{'form': form})

def TodoUpdate(request, key):
    task = models.Task.objects.get(id = key)
    form = forms.TaskForm(instance = task)
    form2 = forms.TaskForm(request.POST, instance= task)
    if form2.is_valid():
        form2.save()
        return redirect('Tasks')
    return render(request, 'TodoUpdate.html', {'form': form})

def TodoDelete(request, key):
    task = models.Task.objects.get(id = key)
    if request.method == 'POST':
        task.delete()
        return redirect('Tasks')
    return render(request, 'TodoDelete.html', {'task': task})

