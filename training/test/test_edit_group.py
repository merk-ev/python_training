# test edit group
# -*- coding: utf-8 -*-
from training.model.group import Group

def test_edit_group(app):
    app.group.edit(Group(name="edit name", header="edit header", footer="edit footer"))
