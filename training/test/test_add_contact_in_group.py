from training.model.contact import Contact
from training.model.group import Group
import random


def test_add_contact_in_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TEST-NAME", middlename="TEST-MIDDLE", lastname="TEST-LAST", bday="01",
                                   bmonth="JANUARY", byear="2000"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    contacts_for_add_in_group = orm.get_contacts_not_in_group(group)
    if contacts_for_add_in_group == []:
        app.contact.add(Contact(firstname="TEST-NAME", middlename="TEST-MIDDLE", lastname="TEST-LAST", bday="01",
                                   bmonth="JANUARY", byear="2000"))
        contact_for_add_in_group = orm.get_contacts_not_in_group(group)[0]
    else:
        contact_for_add_in_group = random.choice(contacts_for_add_in_group)
    app.contact.add_contact_to_group(contact_for_add_in_group, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_for_add_in_group in contacts_in_group
