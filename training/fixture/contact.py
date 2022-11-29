# Helper for contacts

from training.model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        self.go_home()
        # add new contact
        wd.find_element_by_link_text('add new').click()
        self.filling(contact)
        wd.find_element_by_xpath('//div[@id="content"]/form/input[21]').click()
        self.go_home()
        self.contact_cache = None

    def edit_first(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.go_home()
        self.select_contact_by_index_for_edit(index)
        self.filling(contact)
        wd.find_element_by_name('update').click()
        self.go_home()
        self.contact_cache = None

    def select_contact_by_index_for_edit(self, index: int):
        wd = self.app.wd
        wd.find_elements_by_xpath('//img[@alt="Edit"]')[index].click()

    def filling(self, contact):
        wd = self.app.wd
        # fill name
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys(contact.firstname)
        wd.find_element_by_name('middlename').clear()
        wd.find_element_by_name('middlename').send_keys(contact.middlename)
        wd.find_element_by_name('lastname').clear()
        wd.find_element_by_name('lastname').send_keys(contact.lastname)
        wd.find_element_by_name('nickname').clear()
        wd.find_element_by_name('nickname').send_keys(contact.nickname)
        # fill about
        wd.find_element_by_name('title').clear()
        wd.find_element_by_name('title').send_keys(contact.title)
        wd.find_element_by_name('company').clear()
        wd.find_element_by_name('company').send_keys(contact.company)
        # fill contacts
        wd.find_element_by_name('address').clear()
        wd.find_element_by_name('address').send_keys(contact.address)
        wd.find_element_by_name('home').clear()
        wd.find_element_by_name('home').send_keys(contact.home)
        wd.find_element_by_name('mobile').clear()
        wd.find_element_by_name('mobile').send_keys(contact.mobile)
        wd.find_element_by_name('work').clear()
        wd.find_element_by_name('work').send_keys(contact.work)
        wd.find_element_by_name('fax').clear()
        wd.find_element_by_name('fax').send_keys(contact.fax)
        wd.find_element_by_name('email').clear()
        wd.find_element_by_name('email').send_keys(contact.email)
        wd.find_element_by_name('email2').clear()
        wd.find_element_by_name('email2').send_keys(contact.email2)
        wd.find_element_by_name('email3').clear()
        wd.find_element_by_name('email3').send_keys(contact.email3)
        wd.find_element_by_name('homepage').clear()
        wd.find_element_by_name('homepage').send_keys(contact.homepage)
        # fill Bday
        wd.find_element_by_name('bday').send_keys(contact.bday)
        wd.find_element_by_name('bmonth').send_keys(contact.bmonth)
        wd.find_element_by_name('byear').clear()
        wd.find_element_by_name('byear').send_keys(contact.byear)
        wd.find_element_by_name('aday').send_keys(contact.aday)
        wd.find_element_by_name('amonth').send_keys(contact.amonth)
        wd.find_element_by_name('ayear').send_keys(contact.byear)
        wd.find_element_by_name('ayear').send_keys(contact.ayear)
        # fill additional
        wd.find_element_by_name('address2').clear()
        wd.find_element_by_name('address2').send_keys(contact.address2)
        wd.find_element_by_name('phone2').clear()
        wd.find_element_by_name('phone2').send_keys(contact.phone2)
        wd.find_element_by_name('notes').clear()
        wd.find_element_by_name('notes').send_keys(contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_home()
        # select first contact
        self.select_contact_by_index_for_del(index)
        # submit delete
        wd.find_element_by_css_selector('[value="Delete"]').click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector('div.msgbox')
        self.contact_cache = None

    def select_contact_by_index_for_del(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_first_contact_for_del(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def go_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/addressbook/') and len(wd.find_elements_by_name('entry')) > 0):
            wd.find_element_by_link_text('home').click()

    def count(self):
        wd = self.app.wd
        self.go_home()
        return len(wd.find_elements_by_name('selected[]'))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_home()
            self.contact_cache = []
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  address=address, all_phones=all_phones, all_mails=all_mails,))
        return list(self.contact_cache)

    contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_home()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_home()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, home=homephone, work=workphone,
                       mobile=mobilephone, phone2=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search('H: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        return Contact(home=homephone, mobile=mobilephone, work=workphone, phone2=secondaryphone)
