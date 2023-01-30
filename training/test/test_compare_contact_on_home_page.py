# compare contact
import re
from training.model.contact import Contact

# def test_compare_contact_on_home_page(app):
#    contact_from_home_page = app.contact.get_contact_list()[0]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.address == contact_from_edit_page.address
#    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_mails == merge_email_like_on_home_page(contact_from_edit_page)


def test_compare_contacts_on_home_page(app, db):
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(db_contacts) == len(ui_contacts)
    for index in range(len(db_contacts)):
        assert ui_contacts[index].firstname == db_contacts[index].firstname
        assert ui_contacts[index].lastname == db_contacts[index].lastname
        assert ui_contacts[index].address == db_contacts[index].address
        assert ui_contacts[index].all_mails == merge_emails_like_on_home_page(db_contacts[index])
        assert ui_contacts[index].all_phones == merge_phones_like_on_home_page(db_contacts[index])


def clear(string):
    return re.sub('[() /*-]', '', string)


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
