# test delete first contact in list
from training.model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TEST", middlename="Test middle", lastname="Test Last",
                                nickname="TTTT", title="TITlE", company="Company Name", address="RF", home="44-55",
                                mobile="+7-888", work="41-87", fax="47-88", email="e@m.ail", email2="--", email3="---",
                                homepage="home.page", bday="22", bmonth="May", byear="1984", aday="15",
                                amonth="March", ayear="2020", new_group="Test2", address2="street", phone2="non",
                                notes="designer from streets"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
