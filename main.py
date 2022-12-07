from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import threading

from multiprocessing.dummy import Pool as ThreadPool


# Construir el driver, escanea el QR y retorna el driver


def build_driver(i):
    if i == 0:
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
    else:
        driver = webdriver.Firefox()
    driver.get('https://web.whatsapp.com/')
    WebDriverWait(driver, 10000).until(EC.invisibility_of_element_located(
        locator=(By.XPATH, '//div[@data-testid="qrcode"]')))
    WebDriverWait(driver, 10000).until(
        EC.presence_of_element_located(locator=(By.ID, 'side')))
    return driver


def send_message(driver, url, message):
    try:
        driver.get(url)
        time.sleep(5)
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located(locator=(By.ID, 'main')))
        driver.find_element(
            By.XPATH, '//div[@class="_3HQNh _1Ae7k"]').click()
        time.sleep(1)
    except:
        send_message(driver, url, message)


def run(i):
    if i == 0:
        phones = "+573104582173", "+573505168550", "+1(555)008-7322", "+573015089808", "+573023111272", "+573045877319", "+573104582173", "+573505168550", "+1(555)008-7322", "+573015089808", "+573023111272", "+573045877319", "+573104582173", "+573505168550", "+1(555)008-7322", "+573015089808", "+573023111272", "+573045877319"
    else:
        phones = "+1(555)008-7322", "+573015089808", "+573023111272", "+573045877319", "+573104582173", "+573505168550", "+1(555)008-7322", "+573015089808", "+573023111272", "+573045877319", "+573104582173", "+573505168550", "+1(555)008-7322", "+573015089808", "+573023111272", "+573045877319"

    # build_driver(driver)
    driver = build_driver(i)
    # driver2 = build_driver()
    # aux = 0
    for phone in phones:
        message = "Hello World con selenium "
        url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
        # if aux == 0:
        #     send_message(driver, url, message)
        #     aux = 1
        # else:
        #     send_message(driver2, url, message)
        #     aux = 0
        send_message(driver, url, message)

    driver.close()
    # driver2.close()


# run()

# run(0)

pool = ThreadPool()

pool.map(run, range(2))

pool.close()

pool.join()


# phone = "+573045877319"
# message = "Hello World con selenium"
# url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"

# # Construir el driver, escanea el QR y retorna el driver


# def build_driver():
#     driver = webdriver.Chrome(service=ChromeService(
#         ChromeDriverManager().install()))
#     driver.get('https://web.whatsapp.com/')
#     WebDriverWait(driver, 10000).until(EC.invisibility_of_element_located(
#         locator=(By.XPATH, '//div[@data-testid="qrcode"]')))
#     WebDriverWait(driver, 10000).until(
#         EC.presence_of_element_located(locator=(By.ID, 'side')))
#     return driver


# def send_message(driver, url, message):
#     driver.get(url)
#     WebDriverWait(driver, 10000).until(EC.presence_of_element_located(
#         locator=(By.XPATH, '//button[@data-testid="compose-btn-send"]')))
#     driver.find_element(
#         By.XPATH, '//button[@data-testid="compose-btn-send"]').click()
#     time.sleep(0.5)
#     WebDriverWait(driver, 10000).until(EC.text_to_be_present_in_element(
#         (By.XPATH, '//span[@dir="ltr"]'), message))


# driver = build_driver()

# send_message(driver, url, message)
# send_message(driver, url, message)
# send_message(driver, url, message)

# driver.close()
