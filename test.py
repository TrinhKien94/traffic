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
import random
import time
import concurrent.futures
driverLocation = './chromedriver'
def traffic():
    try:
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://vietnam-trader.com")
        # driver.implicitly_wait(30)
        delay = 10 # seconds
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'app-hot-news .table tbody tr:nth-child(2)')))
        javaScript = "$('app-newest-article .article-wrawper:nth-child("+str(random.randint(1,9))+")').click()"
        driver.execute_script(javaScript)
        print("Page is ready!")
        print("Loading took too much time!")
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'app-hot-news-side .card-body:nth-child(2)')))
        javaScript = "$('html, body').animate({scrollTop: $('app-footer').offset().top}, 30000)"
        driver.execute_script(javaScript)
        time.sleep(random.randint(0,120))
        driver.quit()
    except Exception:
        print("Exception")
        driver.quit()
with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    for i in range(0,5000):
        print("loop: "+str(i))
        executor.submit(traffic)
        
# driver.find_element_by_css_selector('app-hot-news .table tbody tr:nth-child(2)').click()
# driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='library_books'])[1]/following::p[1]").click()
# driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='access_time'])[1]/following::h4[1]").click()