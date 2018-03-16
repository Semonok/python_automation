from model.group import Group


def test_add_group(app):
    group = Group(name="1", header="321", footer="195")  # создадим локальную перменную для удобства
    old_groups = app.group_managment.get_group_list()  # длина группы до добавления
    app.group_managment.Create_new_group(group)
    new_groups = app.group_managment.get_group_list()  # длина группы после добавления
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
