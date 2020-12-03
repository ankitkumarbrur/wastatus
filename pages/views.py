from django.shortcuts import render

from wastatus.tasks import fun

# import subprocess
# import shlex

import os

# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def button_view(request):
    os.system('python3 manage.py process_tasks')
    return render(request,'home.html',{})