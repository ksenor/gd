#!/usr/bin/python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys

from s import U_LIST, P_LIST # логины и пароли
from keys import generate_digits as gd

class Gdwinner(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.facebook.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_gdwinner(self):
        driver = self.driver
        for u, p in (U_LIST, P_LIST):
            try:
                POTENTIAL_MONEY_VALS = gd()

                driver.get(self.base_url + "/")
                driver.find_element_by_id("email").clear()
                driver.find_element_by_id("email").send_keys(U)
                driver.find_element_by_id("pass").clear()
                driver.find_element_by_id("pass").send_keys(P)
                driver.find_element_by_id("u_0_n").click()
                driver.get("https://m.facebook.com/www.GD.ru/photos/a.164373060283044.52122.151805011539849/665386580181687")
                time.sleep(5)
                # driver.find_element_by_xpath("//div[contains(@id, 'see_next')]/a/span").click() # поиск существующих
                time.sleep(10)
                # записать значения
                print(POTENTIAL_MONEY_VALS)
                # выйти из аккаунта
            except:
                print('ошибка с %s %s' % (u, p))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
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
