# test/
# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login()
    app.add_new_contact(Contact(firstname="TEST", middlename="Test middle", lastname="Test Last", nickname="TTTT",
                                title="TITlE", company="Company Name", address="RF", home="44-55", mobile="+7-888",
                                work="41-87", fax="47-88", email="e@m.ail", email2="--", email3="---",
                                homepage="home.page", bday="22", bmonth="May", byear="1984", aday="15",
                                amonth="March", ayear="2020", new_group="Test2", address2="street", phone2="non",
                                notes="designer from streets"))
    app.logout()


def test_add_empty_contact(app):
    app.login()
    app.add_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                                homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear="",
                                new_group="", address2="", phone2="", notes=""))
    app.logout()
