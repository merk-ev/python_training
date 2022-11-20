# test edit group
# -*- coding: utf-8 -*-
from training.model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test edit name 1", header="test edit name 2", footer="test edit name 3"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="edit name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test edit header 1", header="test edit header 2", footer="test edit header 3"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(header="edit header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
