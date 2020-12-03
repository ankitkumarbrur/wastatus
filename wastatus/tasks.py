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

print('Background Task')

file = open('/home/ak248100/wastatus/file.txt', 'a')

while(True):
    file.write('background\n')
    time.sleep(2)

file.close()

@background(schedule = 0)
def fun():
    print('BACKGROUND TASK')