from model.group import Group
from random import randrange

def test_modify_group_name(app, groups):  # groups это имя файла с данными для создания и модификации групп
    if app.group_managment.check() is False:  # Проверяем есть ли хоть одна группа
        app.group_managment.Create_new_group(Group(name="12345"))  # Если нет, добавляем
    old_groups = app.group_managment.get_group_list()  # длина группы до изменений
    index = randrange(len(old_groups))  # Создаем переменную с рандомным значением в пределах кол-ва групп
    group = groups  # Создаем локальную перемнную для удобства
    group.id = old_groups[index].id  # id группы после изменения равен id изменяемой группы
    app.group_managment.modify_group(group, index)  # модифицируем группу с индексом, обявленным ранее
    new_groups = app.group_managment.get_group_list()  # длина группы после изменений
    assert len(old_groups) == len(new_groups)  # Сравниваем длину до и после
    old_groups[index] = group  # Меняем первую группу в старой группе, на модифицированную
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)  # Сортируем по ключу при сравнении


#def test_modify_group_header(app):
#    app.group_managment.modify_group(Group(header="Bomber"))


#def test_modify_group_footer(app):
#    app.group_managment.modify_group(Group(footer="Bomberman"))


#def test_modify_group_full(app):
#    app.group_managment.modify_group(Group(name="pups", header="pupus", footer="pupupus"))
