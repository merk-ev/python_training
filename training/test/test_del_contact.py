def test_delete_first_contact(app):
    app.session.login()
    app.contact.delete_first_contact()
    app.session.logout()
