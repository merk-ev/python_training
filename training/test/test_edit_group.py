# test edit group
# -*- coding: utf-8 -*-
from training.model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="edit name", header="edit header", footer="edit footer"))
    app.session.logout()
