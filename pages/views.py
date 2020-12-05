from django.shortcuts import render

from wastatus.tasks import fun

import subprocess
import shlex

import os
import time

# Create your views here.
def home_view(request):
    subprocess.Popen(". /home/ak248100/wastatus/my_env/bin/activate && python3 /home/ak248100/wastatus/manage.py process_tasks", shell=True)
    return render(request,'home.html',{})

def button_view(request):
    fun()
    time.sleep(5)
    return render(request,'home.html',{})