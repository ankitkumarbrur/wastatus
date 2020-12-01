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

chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1280x722")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# driver = webdriver.Chrome(r'C:\Users\Ankit\Documents\Django\projects\wastatus\wastatus\chromedriver.exe',options=chrome_options)
driver = webdriver.Chrome(executable_path=r"/usr/local/lib/chromedriver",options=chrome_options)

driver.get('https://web.whatsapp.com')

el = driver.find_elements_by_class_name('landing-main')

el[0].screenshot("./screenshot.png")

@background(schedule = 0)
def fun():
    print('BACKGROUND TASK')