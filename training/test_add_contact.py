# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contat(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Test")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Testovich")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Testoviy")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("Tester78")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("Company")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Address")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Address")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("+7123456789")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("+7777777777")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("+6666666666")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("+6666666665")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("e-mail@e.mail")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("-")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("--")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("home.apge")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("30")
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("February")
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1990")
        Select(driver.find_element_by_name("aday")).select_by_visible_text("30")
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("February")
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2020")
        Select(driver.find_element_by_name("new_group")).select_by_visible_text("Test 1")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("non")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("empty")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("designer from SF")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("home").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
