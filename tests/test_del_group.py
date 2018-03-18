from model.group import Group
from random import randrange


def test_del_group(app):
    if app.group_managment.check() is False:
        app.group_managment.Create_new_group(Group(name="12345"))
    old_groups = app.group_managment.get_group_list()  # длина группы до удаления
    index = randrange(len(old_groups))
    app.group_managment.delete_group(index)
    new_groups = app.group_managment.get_group_list()  # длина группы после удаления
    assert len(old_groups) - 1 == len(new_groups)
    # Создаем проверку элементов группы
    del old_groups[index]
    assert old_groups == new_groups
