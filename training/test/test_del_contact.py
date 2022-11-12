# test delete first contact in list
from training.model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="TESTOVIY", middlename="TESTOVIY", lastname="TESTOVIY",
                                   nickname="TESTOVIY", title=" ", company=" ", address=" ",
                                   home=" ", mobile=" ", work=" ", fax=" ", email=" ",
                                   email2=" ", email3=" ", homepage=" ", bday=" ", bmonth=" ",
                                   byear=" ", aday=" ", amonth=" ", ayear=" ", new_group=" ",
                                   address2=" ", phone2=" ", notes=" "))
    app.contact.delete_first_contact()
