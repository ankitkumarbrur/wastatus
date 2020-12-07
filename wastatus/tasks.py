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

from datetime import datetime
import boto3

from django.utils.timezone import get_current_timezone
from status.models import Status

print('BACKGROUND TASK')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path="/home/ak248100/wastatus/wastatus/chromedriver", options=chrome_options)
# driver = webdriver.Chrome(r"C:\Users\Ankit\Documents\Django\projects\wastatus\wastatus\chromedriver.exe")


@background(schedule = 0)
def load_qr():
    print('LOAD QR')
    driver.get("https://web.whatsapp.com/")

    time.sleep(2)
    
    ele = driver.find_elements_by_class_name('landing-main')

    ele[0].screenshot("/home/ak248100/wastatus/static/screenshot.png")

    s3_client = boto3.client('s3', aws_access_key_id='AKIAYC7ISQDUY2HJSMM4', aws_secret_access_key= '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')
    response = s3_client.upload_file('/home/ak248100/wastatus/static/screenshot.png', 'ankitwstatus', 'screenshot.png')


@background(schedule = 0)
def current_screen():
    driver.save_screenshot("/home/ak248100/wastatus/static/screenshot.png")

    s3_client = boto3.client('s3', aws_access_key_id='AKIAYC7ISQDUY2HJSMM4', aws_secret_access_key= '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')
    response = s3_client.upload_file('/home/ak248100/wastatus/static/screenshot.png', 'ankitwstatus', 'screenshot.png')

@background(schedule = 0)
def start_tracking():
    print("Tracking")
    
    status = False
    target = '"Riddhi"'
    x_arg = '//span[contains(@title,' + target + ')]'

    wait = WebDriverWait(driver, 600)
    search = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_1awRl')))
    search.click()

    search.send_keys("Ankit1")

    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()

    time.sleep(5)

    while (True):
        if(driver.find_elements_by_xpath('.//span[@title = "online"]') and status == False):
            status = True

            print('fun')
            on = datetime.now(tz=get_current_timezone())

            print(target + ' came online at ' + on.strftime('%H:%M:%S'))

        elif(not(driver.find_elements_by_xpath('.//span[@title = "online"]')) and status == True ):
            status = False

            off = datetime.now(tz=get_current_timezone())
            
            diff = off-on

            Status.objects.create(online=on,offline=off,duration=diff)

            print(target + ' went offline at ' + off.strftime('%H:%M:%S'))
        elif(datetime.now().minute % 2 == 0 and datetime.now().second == 0):
            print('ping')
            element = driver.find_elements_by_xpath('.//div[@title = "Menu"]')
            element[1].click()

    driver.quit()

    # driver.save_screenshot("/home/ak248100/wastatus/static/screenshot.png")
    # s3_client = boto3.client('s3', aws_access_key_id='AKIAYC7ISQDUY2HJSMM4', aws_secret_access_key= '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')
    # response = s3_client.upload_file('/home/ak248100/wastatus/static/screenshot.png', 'ankitwstatus', 'screenshot.png')