from django.views.decorators.cache import never_cache
from django.shortcuts import render

from wastatus.tasks import load_qr
from wastatus.tasks import current_screen
from wastatus.tasks import start_tracking

import subprocess
import shlex

import os
import time

# Create your views here.
@never_cache
def home_view(request):
    return render(request,'home.html',{})

@never_cache
def background_view(request):
    subprocess.Popen(". /home/ak248100/wastatus/my_env/bin/activate && python3 /home/ak248100/wastatus/manage.py process_tasks", shell=True)
    return render(request,'home.html',{})

@never_cache
def qr_view(request):
    load_qr()
    time.sleep(5)
    return render(request,'home.html',{})

@never_cache
def current_view(request):
    current_screen()
    return render(request,'screen.html',{})

@never_cache
def track_view(request):
    start_tracking()
    return render(request,'home.html',{})