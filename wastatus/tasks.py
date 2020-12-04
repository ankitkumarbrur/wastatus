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

print('BACKGROUND TASK')

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--headless")
chromeoptions.add_argument("--disable-dev-shm-usage")
chromeoptions.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path="/home/ak248100/wastatus/wastatus/chromedriver", options=chromeoptions)

driver.get("www.google.com")

driver.save_screenshot('/home/ak248100/wastatus/screenshot.png')

driver.quit()

@background(schedule = 0)
def fun():
    print('FUN')
    t = 0
    file = open('/home/ak248100/wastatus/file.txt', 'a')
    while (t <= 10):
        t = t+1
        file.write('\nbackground from fun' + str(t))
        time.sleep(2)
    file.close()