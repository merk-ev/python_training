# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class TestAddContat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.driver.implicitly_wait(30)

    def test_add_contat(self):
        driver = self.driver
        # open home page
        driver.get("http://localhost/addressbook/")
        # login
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        # add new contact
        driver.find_element_by_link_text("add new").click()
        # fill name
        driver.find_element_by_name("firstname").send_keys("Test")
        driver.find_element_by_name("middlename").send_keys("Testovich")
        driver.find_element_by_name("lastname").send_keys("Testoviy")
        driver.find_element_by_name("nickname").send_keys("Tester78")
        # fill about
        driver.find_element_by_name("title").send_keys("Title")
        driver.find_element_by_name("company").send_keys("Company")
        # fill contacts
        driver.find_element_by_name("address").send_keys("Address")
        driver.find_element_by_name("address").send_keys("Address")
        driver.find_element_by_name("home").send_keys("+7123456789")
        driver.find_element_by_name("mobile").send_keys("+7777777777")
        driver.find_element_by_name("work").send_keys("+6666666666")
        driver.find_element_by_name("fax").send_keys("+6666666665")
        driver.find_element_by_name("email").send_keys("e-mail@e.mail")
        driver.find_element_by_name("email2").send_keys("-")
        driver.find_element_by_name("email3").send_keys("--")
        driver.find_element_by_name("homepage").send_keys("home.apge")
        # fill Bday
        driver.find_element_by_name("bday").send_keys("30")
        driver.find_element_by_name("bmonth").send_keys("February")
        driver.find_element_by_name("byear").send_keys("1990")
        driver.find_element_by_name("aday").send_keys("30")
        driver.find_element_by_name("amonth").send_keys("February")
        driver.find_element_by_name("ayear").send_keys("2020")
        # choose group
        driver.find_element_by_name("new_group").send_keys("Test 1")
        # fill additional
        driver.find_element_by_name("address2").send_keys("non")
        driver.find_element_by_name("phone2").send_keys("empty")
        driver.find_element_by_name("notes").send_keys("designer from SF")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # go to home
        driver.find_element_by_link_text("home").click()
        # logout
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

if __name__ == "__main__":
    unittest.main()
