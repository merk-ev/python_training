# test edit group
# -*- coding: utf-8 -*-
from training.model.group import Group

def test_edit_group_name(app):
    app.group.edit_first(Group(name="edit name"))

def test_edit_group_header(app):
    app.group.edit_first(Group(header="edit header"))
