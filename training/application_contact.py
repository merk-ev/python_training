# fixture
from selenium import webdriver


class ApplicationContact:

    def __init__(self):
        self.driver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.driver.implicitly_wait(30)

    def logout(self):
        driver = self.driver
        # logout
        driver.find_element_by_link_text("Logout").click()

    def go_home(self):
        driver = self.driver
        # go home
        driver.find_element_by_link_text("home").click()

    def add_new_contact(self, contact):
        driver = self.driver
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
        self.go_home()

    def login(self):
        driver = self.driver
        self.open_home_page()
        # login
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        # open home page
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()