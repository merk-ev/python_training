from training.model.contact import Contact
from training.model.group import Group
import random

def test_delete_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="group test", footer="test group"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TEST-NAME", middlename="TEST-MIDDLE", lastname="TEST-LAST", bday="01",
                                   bmonth="JANUARY", byear="2000"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.del_contact_by_id_from_group(contact, group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert contacts_in_group not in new_contacts_in_group
