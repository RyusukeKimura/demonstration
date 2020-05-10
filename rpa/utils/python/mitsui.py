# import libraries
import time
from datetime import datetime

# import selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_driver(driver, timeout, id):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, id)))
    except:
        print('retry')
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, id)))
    time.sleep(1)

# move to search result page from search page
def move_to_search_result_page_from_search_page(driver, timeout):
    wait_driver(driver, timeout, 'active')
    xpath = '//*[@id="active"]'
    driver.find_element_by_xpath(xpath).click()

# move to search page from top page
def move_to_search_page_from_top_page(driver, timeout):
    wait_driver(driver, timeout, 'main')
    xpath = '//*[@id="main"]/div[1]/div[1]/div[2]/div[1]/a'
    driver.find_element_by_xpath(xpath).click()

def extract_information(driver, todofuken, shikuchoson, timeout):
    # extract information
    ## first block
    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[1]/tbody/tr[1]/td'
    bld_name = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[1]/tbody/tr[2]/td'
    room_name = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[1]/tbody/tr[3]/td'
    room_madori = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[1]/tbody/tr[5]/td'
    bld_address = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[1]/tbody/tr[6]/td'
    access = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[1]/tbody/tr[7]/td'
    num_rooms = driver.find_element_by_xpath(xpath).text

    ## second block
    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[1]/td[1]'
    chinryo = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[1]/td[2]'
    kanrihi = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[2]/td[1]'
    sikikin = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[2]/td[2]'
    reikin = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[3]/td'
    kibo_kozo = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[4]/td[1]'
    menseki_tsubo = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[4]/td[2]'
    syunko_nengappi = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[5]/td[1]'
    nyukyo_kanoubi = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[5]/td[2]'
    annai_kanoubi = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[6]/td[1]'
    keiyaku_kikan = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[6]/td[2]'
    kousinryo = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[7]/td[1]'
    torihiki_taiyo = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[7]/td[2]'
    parking = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[8]/td'
    hoken = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[9]/td'
    kanri_gaisya = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[10]/td[1]'
    kagi_koukan = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[10]/td[2]'
    kouza_furikae = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[11]/td'
    hosyo_gaisya = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[12]/td'
    setsubi = driver.find_element_by_xpath(xpath).text

    xpath = '//*[@id="container"]/section/div[1]/div/div/div[1]/table[2]/tbody/tr[13]/td'
    bikou = driver.find_element_by_xpath(xpath).text

    dt_now = datetime.now

    array = [dt_now, todofuken, shikuchoson, bld_name, room_name, room_madori, bld_address, access, num_rooms,
                    chinryo, kanrihi, sikikin, reikin, kibo_kozo, menseki_tsubo, syunko_nengappi, keiyaku_kikan, kousinryo,
                   torihiki_taiyo, parking, hoken, kanri_gaisya, kagi_koukan, kouza_furikae, hosyo_gaisya, setsubi, bikou]

    return array