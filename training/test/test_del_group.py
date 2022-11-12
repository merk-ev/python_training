# test delete first group in list
from training.model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test delete", header="test delete header", footer='test delete footer'))
    app.group.delete_first_group()
