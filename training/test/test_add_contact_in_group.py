from training.model.contact import Contact
from training.model.group import Group
import random


def test_add_contact_in_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname='TEST', middlename='Test middle', lastname='Test Last',
                                nickname='TTTT', title='TITlE', company='Company Name', address='RF', home='44-55',
                                mobile='+7-888', work='41-87', fax='47-88', email='e@m.ail', email2='--', email3='---',
                                homepage='home.page', bday='22', bmonth='May', byear='1984', aday='15',
                                amonth='March', ayear='2020', new_group='Test2', address2='street', phone2='non',
                                notes='designer from streets'))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    contacts_for_add_in_group = orm.get_contacts_not_in_group(group)
    if contacts_for_add_in_group == []:
        app.contact.add_new(Contact(firstname='TEST', middlename='Test middle', lastname='Test Last',
                                nickname='TTTT', title='TITlE', company='Company Name', address='RF', home='44-55',
                                mobile='+7-888', work='41-87', fax='47-88', email='e@m.ail', email2='--', email3='---',
                                homepage='home.page', bday='22', bmonth='May', byear='1984', aday='15',
                                amonth='March', ayear='2020', new_group='Test2', address2='street', phone2='non',
                                notes='designer from streets'))
        contact_for_add_in_group = orm.get_contacts_not_in_group(group)[0]
    else:
        contact_for_add_in_group = random.choice(contacts_for_add_in_group)
    app.contact.add_contact_to_group(contact_for_add_in_group, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_for_add_in_group in contacts_in_group
