# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://csgoempire.com/history?seed=1023')
# print(r.status)
# print(r.data)
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://vietnam-trader.com")
# driver.implicitly_wait(30)
delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'app-hot-news .table tbody tr:nth-child(2)')))
    javaScript = "$('app-hot-news .table tbody tr:nth-child(2)').click()"
    driver.execute_script(javaScript)
    print("Page is ready!")
except Exception:
    print("Loading took too much time!")
# driver.find_element_by_css_selector('app-hot-news .table tbody tr:nth-child(2)').click()
# driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='library_books'])[1]/following::p[1]").click()
# driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='access_time'])[1]/following::h4[1]").click()
input("Enter for continue:")