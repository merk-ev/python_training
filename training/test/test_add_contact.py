# test adding contact
# -*- coding: utf-8 -*-
from training.model.contact import Contact


def test_add_contact(app):
     old_contacts = app.contact.get_contact_list()
     contact = Contact(firstname='TEST', middlename='Test middle', lastname='Test Last',
                                nickname='TTTT', title='TITlE', company='Company Name', address='RF', home='44-55',
                                mobile='+7-888', work='41-87', fax='47-88', email='e@m.ail', email2='--', email3='---',
                                homepage='home.page', bday='22', bmonth='May', byear='1984', aday='15',
                                amonth='March', ayear='2020', new_group='Test2', address2='street', phone2='non',
                                notes='designer from streets')
     app.contact.add_new(contact)
     assert len(old_contacts) + 1 == app.contact.count()
     new_contacts = app.contact.get_contact_list()
     old_contacts.append(contact)
     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
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
