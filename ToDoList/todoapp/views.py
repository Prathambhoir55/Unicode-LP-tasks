from django.shortcuts import render, redirect
from django.urls.base import reverse
from . import forms
from . import models
import requests
from accounts.models import MyUser


def TodoHome(request):
    pk = request.user.id
    Tasks = models.Task.objects.filter(task_user = pk)
    return render(request,'TodoHome.html', {'Tasks': Tasks, 'pk': pk})

def TodoCreate(request, pk):
    form = forms.TaskForm()

    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form1 = form.save(commit= False)
            user =MyUser.objects.get(id = pk)
            form1.task_user = user
            form1.save() 
            return redirect ('home')
    return render(request, 'TodoCreate.html',{'form': form})

def TodoUpdate(request, key):
    task = models.Task.objects.get(id = key)
    form = forms.TaskForm(instance = task)
    form2 = forms.TaskForm(request.POST, instance= task)
    if form2.is_valid():
        form2.save()
        return redirect('home')
    return render(request, 'TodoUpdate.html', {'form': form})

def TodoDelete(request, key):
    task = models.Task.objects.get(id = key)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'TodoDelete.html', {'task': task})

