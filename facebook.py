# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
driverLocation = './chromedriver' 
driver = webdriver.Chrome(driverLocation)
driver.get("https://www.facebook.com/%C4%90%C3%A0o-V%C4%83n-Chung-104007340976342/")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Việc sử dụng Bitcoin ngày càng tăng khi số lượng máy ATM tiền điện tử tăng gần 500% trong 3 năm'])[2]/following::a[1]").click()# time.sleep(60)
# driver.quit()
# class UntitledTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://www.katalon.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
    
#     def test_untitled_test_case(self):
#         driver = self.driver
#         driver.get("https://www.facebook.com/%C4%90%C3%A0o-V%C4%83n-Chung-104007340976342/")
#         driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Việc sử dụng Bitcoin ngày càng tăng khi số lượng máy ATM tiền điện tử tăng gần 500% trong 3 năm'])[2]/following::a[1]").click()
#         # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
#         # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
    
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
