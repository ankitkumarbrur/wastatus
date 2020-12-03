from django.shortcuts import render

from wastatus.tasks import fun

import subprocess
import shlex


# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def button_view(request):
    process_tasks_cmd = "sudo reeboot"
    process_tasks_args = shlex.split(process_tasks_cmd)
    subprocess.Popen(process_tasks_args)
    return render(request,'home.html',{})