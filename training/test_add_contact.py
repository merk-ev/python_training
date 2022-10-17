# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.add_new_contact(driver, Contact(firstname = "TEST", middlename = "Test middle", lastname = "Test Last",
                                             nickname = "TTTT", title = "TITlE", company = "Company Name",
                                             address = "RF",  home = "44-55", mobile = "+7-888", work = "41-87",
                                             fax = "47-88", email = "e@m.ail", email2 = "--", email3 = "---",
                                             homepage = "home.page", bday = "22", bmonth = "May", byear = "1984",
                                             aday = "15", amonth = "March",  ayear = "2020", new_group = "Test2",
                                             address2 = "street", phone2 = "non", notes = "designer from streets"))
        self.go_home(driver)
        self.logout(driver)

    def test_add_empty_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.add_new_contact(driver, Contact(firstname="", middlename="", lastname="",
                                                 nickname="", title="", company="",
                                                 address="", home="", mobile="", work="",
                                                 fax="", email="", email2="", email3="",
                                                 homepage="", bday="", bmonth="", byear="",
                                                 aday="", amonth="", ayear="", new_group="",
                                                 address2="", phone2="", notes=""))
        self.go_home(driver)
        self.logout(driver)

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text("Logout").click()

    def go_home(self, driver):
        # go to home
        driver.find_element_by_link_text("home").click()

    def add_new_contact(self, driver, contact):
        # add new contact
        driver.find_element_by_link_text("add new").click()
        # fill name
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        # fill about
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").send_keys(contact.company)
        # fill contacts
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").send_keys(contact.home)
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("work").send_keys(contact.work)
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").send_keys(contact.email3)
        driver.find_element_by_name("homepage").send_keys(contact.homepage)
        # fill Bday
        driver.find_element_by_name("bday").send_keys(contact.bday)
        driver.find_element_by_name("bmonth").send_keys(contact.bmonth)
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_name("aday").send_keys(contact.aday)
        driver.find_element_by_name("amonth").send_keys(contact.amonth)
        driver.find_element_by_name("ayear").send_keys(contact.ayear)
        # choose group
        driver.find_element_by_name("new_group").send_keys(contact.new_group)
        # fill additional
        driver.find_element_by_name("address2").send_keys(contact.address2)
        driver.find_element_by_name("phone2").send_keys(contact.phone2)
        driver.find_element_by_name("notes").send_keys(contact.notes)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, driver):
        # login
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        # open home page
        driver.get("http://localhost/addressbook/")

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
