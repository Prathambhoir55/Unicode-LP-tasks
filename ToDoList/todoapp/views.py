from django.shortcuts import render
import requests


def TodoHome(request):
    return render(request,'TodoHome.html')

def TodoInput(request):
    name=request.POST.get('taskname')
    time=request.POST.get('tasktime')
    return render(request,'TodoInput.html',{'name': name, 'time': time})
