from model.group import Group


def test_add_group(app):
    old_groups = app.group_managment.get_group_list()  # длина группы до добавления
    app.group_managment.Create_new_group(Group(name="123", header="321", footer="195"))
    new_groups = app.group_managment.get_group_list()  # длина группы после добавления
    assert len(old_groups) + 1 == len(new_groups)

