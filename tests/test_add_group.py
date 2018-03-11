from model.group import Group


def test_add_group(app):
    app.group_managment.Create_new_group(Group(name="123", header="321", footer="195"))

