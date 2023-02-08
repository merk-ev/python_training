from training.model.contact import Contact
from training.model.group import Group
import random

def test_delete_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname='TEST', middlename='Test middle', lastname='Test Last',
                                nickname='TTTT', title='TITlE', company='Company Name', address='RF', home='44-55',
                                mobile='+7-888', work='41-87', fax='47-88', email='e@m.ail', email2='--', email3='---',
                                homepage='home.page', bday='22', bmonth='May', byear='1984', aday='15',
                                amonth='March', ayear='2020', new_group='Test2', address2='street', phone2='non',
                                notes='designer from streets'))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.del_contact_by_id_from_group(contact, group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert contacts_in_group not in new_contacts_in_group
