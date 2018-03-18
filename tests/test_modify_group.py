from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group_managment.check() is False:
        app.group_managment.Create_new_group(Group(name="12345"))
    old_groups = app.group_managment.get_group_list()  # длина группы до изменений
    index = randrange(len(old_groups))
    group = Group(name="Bomb")  # Создаем локальную перемнную для удобства
    group.id = old_groups[index].id
    app.group_managment.modify_group(group, index)
    new_groups = app.group_managment.get_group_list()  # длина группы после изменений
    assert len(old_groups) == len(new_groups)  # Сравниваем длину до и после
    old_groups[index] = group  # Меняем первую группу в старой группе, на модифицированную
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    app.group_managment.modify_group(Group(header="Bomber"))


#def test_modify_group_footer(app):
#    app.group_managment.modify_group(Group(footer="Bomberman"))


#def test_modify_group_full(app):
#    app.group_managment.modify_group(Group(name="pups", header="pupus", footer="pupupus"))
