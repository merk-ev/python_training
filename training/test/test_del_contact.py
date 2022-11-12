# test delete first contact in list
def test_delete_first_contact(app):
    app.contact.delete_first_contact()
