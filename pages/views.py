from django.shortcuts import render

from wastatus.tasks import fun

import subprocess
import shlex


# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def button_view(request):
    return render(request,'home.html',{})