# test edit contact
# -*- coding: utf-8 -*-
from training.model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname='TEST', middlename='Test middle', lastname='Test Last',
                                nickname='TTTT', title='TITlE', company='Company Name', address='RF', home='44-55',
                                mobile='+7-888', work='41-87', fax='47-88', email='e@m.ail', email2='--', email3='---',
                                homepage='home.page', bday='22', bmonth='May', byear='1984', aday='15',
                                amonth='March', ayear='2020', new_group='Test2', address2='street', phone2='non',
                                notes='designer from streets'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname='EDIT', middlename='EDIT', lastname='EDIT',
                                   nickname='EEEE', title='EDIT TITLE', company='EDIT COMPANY', address='ED-IT',
                                   home='44-22', mobile='+7-888', work='41-87', fax='47-88', email='e@m.ail',
                                   email2='--', email3='---', homepage='home.page', bday='22', bmonth='May',
                                   byear='1984', aday='15', amonth='March', ayear='2020', new_group='Test2',
                                   address2='street', phone2='non', notes='EDITED')
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
