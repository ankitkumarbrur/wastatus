from django.shortcuts import render

from wastatus.tasks import fun

# import subprocess
# import shlex

import os

# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def button_view(request):
    out = os.system('python3 manage.py runserver')
    return render(request,'home.html',{'exit': out})