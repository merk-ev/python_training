# test edit group
# -*- coding: utf-8 -*-
from training.model.group import Group
from random import randrange


def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name='test edit name 1', header='test edit name 2', footer='test edit name 3'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='edit name')
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

