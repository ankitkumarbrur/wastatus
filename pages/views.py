from django.shortcuts import render

from wastatus.tasks import fun

# import subprocess
# import shlex

import os

# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def button_view(request):
    out = os.system('sudo reboot')
    print("cmd ran with exit code %d" % out)
    return render(request,'home.html',{})