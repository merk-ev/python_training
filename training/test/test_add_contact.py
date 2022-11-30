# test adding contact
# -*- coding: utf-8 -*-
from training.model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    digits = string.digits
    return ''.join([random.choice(digits) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname='', middlename='', lastname='', nickname='', title='', company='', address='', home='',
                    mobile='', work='', fax='', email='', email2='', email3='', homepage='', bday='', bmonth='',
                    byear='', aday='', amonth='', ayear='', address2='', phone2='', notes='')] + [
    Contact(firstname=random_string('firstname-', 10),  middlename=random_string('middlename-', 10),
            lastname=random_string('lastname-', 10), nickname=random_string('nickname-', 10),
            title=random_string('title-', 10), company=random_string('company-', 10),
            address=random_string('address-', 10), home=random_digits(10), mobile=random_digits(10),
            work=random_digits(10), fax=random_digits(10), email=random_string('email-', 10),
            email2=random_string('email2-', 10), email3=random_string('email3-', 10),
            homepage=random_string('homepage-', 10), bday=random_digits(2), bmonth=random_digits(2),
            byear=random_digits(4), aday=random_digits(2), amonth=random_digits(2),
            ayear=random_digits(4), address2=random_string('address2-', 10),
            phone2=random_digits(10), notes=random_string('notes-', 30))
    for i in range(5)]



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
     old_contacts = app.contact.get_contact_list()
     app.contact.add_new(contact)
     assert len(old_contacts) + 1 == app.contact.count()
     new_contacts = app.contact.get_contact_list()
     old_contacts.append(contact)
     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname='', middlename='', lastname='', nickname='', title='', company='',
#                                address='', home='', mobile='', work='', fax='', email='', email2='', email3='',
#                                homepage='', bday='', bmonth='', byear='', aday='', amonth='', ayear='',
#                                new_group='', address2='', phone2='', notes='')
#    app.contact.add_new(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
