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
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").click()
driver.find_element_by_name("q").send_keys(Keys.DOWN)
driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys("vietnam-trader")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.find_element_by_link_text("2").click()
driver.find_element_by_link_text("3").click()
driver.find_element_by_link_text("4").click()
driver.find_element_by_link_text("5").click()
driver.find_element_by_link_text("6").click()
driver.find_element_by_link_text("3").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vietnamese trader'])[1]/following::div[5]").click()


# driverLocation = './chromedriver' 
# with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
#     for i in range(0,500):
#         # executor.map(self.getWebContent, (url,))
#         driver = webdriver.Chrome(driverLocation)
#         driver.get("https://vietnam-trader.com")
#         # driver.implicitly_wait(30)
#         delay = 10 # seconds
#         try:
#             myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'app-hot-news .table tbody tr:nth-child(2)')))
#             javaScript = "$('app-newest-article .article-wrawper:nth-child("+str(random.randint(1,9))+")').click()"
#             driver.execute_script(javaScript)
#             print("Page is ready!")
#         except Exception:
#             print("Loading took too much time!")
#         myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'app-hot-news-side .card-body:nth-child(2)')))
#         javaScript = "$('html, body').animate({scrollTop: $('app-footer').offset().top}, 1000)"
#         driver.execute_script(javaScript)
#         # time.sleep(60)
#         driver.quit()
# # driver.find_element_by_css_selector('app-hot-news .table tbody tr:nth-child(2)').click()
# # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='library_books'])[1]/following::p[1]").click()
# # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='access_time'])[1]/following::h4[1]").click()


# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re

# class UntitledTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://www.katalon.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
    
#     def test_untitled_test_case(self):
#         driver = self.driver
#         driver.get("https://www.google.com/")
#         driver.find_element_by_name("q").click()
#         driver.find_element_by_name("q").send_keys(Keys.DOWN)
#         driver.find_element_by_name("q").clear()
#         driver.find_element_by_name("q").send_keys("vietnam-trader")
#         driver.find_element_by_name("q").send_keys(Keys.ENTER)
#         driver.find_element_by_link_text("2").click()
#         driver.find_element_by_link_text("3").click()
#         driver.find_element_by_link_text("4").click()
#         driver.find_element_by_link_text("5").click()
#         driver.find_element_by_link_text("6").click()
#         driver.find_element_by_link_text("3").click()
#         driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vietnamese trader'])[1]/following::div[5]").click()
    
#     def is_element_present(self, how, what):
#         try: self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e: return False
#         return True
    
#     def is_alert_present(self):
#         try: self.driver.switch_to_alert()
#         except NoAlertPresentException as e: return False
#         return True
    
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally: self.accept_next_alert = True
    
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)

# if __name__ == "__main__":
#     unittest.main()
