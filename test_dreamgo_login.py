# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestDreamgoLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://192.168.1.102/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_dreamgo_login(self):
        driver = self.driver
        driver.get(self.base_url + "/test_dreamgo/app/#/homepage")
        driver.implicitly_wait(10)
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("15856691310")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("luhu199515lbh", Keys.ENTER)
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        response = driver.find_element_by_class_name("ng-binding").text
        self.assertEqual(u'卢虎', response)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()