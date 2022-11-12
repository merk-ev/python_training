# test adding group
# -*- coding: utf-8 -*-
from training.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Test 2", header="header 2", footer="footer 2"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
