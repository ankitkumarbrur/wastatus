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

options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
options.add_argument('--headless')
# chrome_options.add_argument("--window-size=1280x722")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

# driver = webdriver.Chrome(r'C:\Users\Ankit\Documents\Django\projects\wastatus\wastatus\chromedriver.exe',options=chrome_options)
driver = webdriver.Chrome('/home/ak248100/wastatus/wastatus/chromedriver',options=options)

file = open('file.txt','r')
file.close()
# driver.get('https://web.whatsapp.com')

# el = driver.find_elements_by_class_name('landing-main')

# el[0].screenshot("./screenshot.png")

@background(schedule = 0)
def fun():
    print('BACKGROUND TASK')