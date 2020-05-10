# import libraries
import time
from datetime import datetime

# import selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_id_pass():
    f = open('id_pass.txt')
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    id, pw = lines[0], lines[1]
    return id, pw


def wait_driver(driver, timeout, id):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, id)))
    except TimeoutException:
        print('retry')
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, id)))
    time.sleep(5)