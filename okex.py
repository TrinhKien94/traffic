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
import os
import sys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import concurrent.futures
# driverLocation = './chromedriver'
os.environ['MOZ_HEADLESS'] = '1'
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)
binary.add_command_line_options('-headless') 
with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
    for i in range(0,2000):
        # executor.map(self.getWebContent, (url,))
        print("count = "+str(i))
        driver = webdriver.Firefox(firefox_binary=binary)
        driver.get("https://www.okex.com/")
        driver.implicitly_wait(10)
        # delay = 10 # seconds
        # try:
        #     myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'app-hot-news .table tbody tr:nth-child(2)')))
        #     javaScript = "$('app-newest-article .article-wrawper:nth-child("+str(random.randint(1,9))+")').click()"
        #     driver.execute_script(javaScript)
        #     print("Page is ready!")
        # except Exception:
        #     print("Loading took too much time!")
        # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'app-hot-news-side .card-body:nth-child(2)')))
        # javaScript = "$('html, body').animate({scrollTop: $('app-footer').offset().top}, 1000)"
        # driver.execute_script(javaScript)
        # # time.sleep(60)
        driver.quit()
# driver.find_element_by_css_selector('app-hot-news .table tbody tr:nth-child(2)').click()
# driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='library_books'])[1]/following::p[1]").click()
# driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='access_time'])[1]/following::h4[1]").click()