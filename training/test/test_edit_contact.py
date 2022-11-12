# test edit contact
# -*- coding: utf-8 -*-
from training.model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first(Contact(firstname="EDIT", middlename="EDIT MIDDLE", lastname="EDIT Last",
                                   nickname="EEEE", title="EDIT TITLE", company="EDIT COMPANY", address="ED-IT",
                                   home="44-22", mobile="+7-888", work="41-87", fax="47-88", email="e@m.ail",
                                   email2="--", email3="---", homepage="home.page", bday="22", bmonth="May",
                                   byear="1984", aday="15", amonth="March", ayear="2020", new_group="Test2",
                                   address2="street", phone2="non", notes="EDITED"))
