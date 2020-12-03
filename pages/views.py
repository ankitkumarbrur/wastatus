from django.shortcuts import render

from wastatus.tasks import fun

import subprocess
import shlex

import os

# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def button_view(request):
    pr = shlex.split("cd /home/ak248100/wastatus && python3 manage.py process_tasks")
    process_ta = subprocess.Popen(pr)
    return render(request,'home.html',{})