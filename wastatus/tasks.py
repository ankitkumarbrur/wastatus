from background_task import background
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import os

file = open('file.txt','a')
file.write("I am running in background")
file.close()

print('Background Task')

@background(schedule = 0)
def fun():
    print('BACKGROUND TASK')