import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_login:
    def test_logintest(self):

        username=self.driver.find_element(By.XPATH,"//input[@name='username']")
        username.send_keys("yashcarcrazy")
        password=self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.send_keys("sachin@123")
        time.sleep(2)
        log_in=self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        log_in.click()
        time.sleep(5)