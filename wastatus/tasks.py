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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path="/home/ak248100/wastatus/wastatus/chromedriver", options=chrome_options)

driver.get("https://web.whatsapp.com/")

driver.save_screenshot('/home/ak248100/wastatus/static/screenshot.png')

driver.quit()

@background(schedule = 0)
def fun():
    print('FUN')
    t = 0
    file = open('/home/ak248100/wastatus/file.txt', 'a')
    while (t <= 10):
        t = t+1
        file.write('\nI am from fun' + str(t))
        time.sleep(2)
    file.close()