from django.shortcuts import render

from wastatus.tasks import fun

import subprocess
import shlex

import os

# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def button_view(request):
    subprocess.Popen("cd /home/ak248100/wastatus/my_env/bin/activate ", shell=True)
    return render(request,'home.html',{})