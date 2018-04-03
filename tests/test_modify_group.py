from model.group import Group
from random import randrange, choice


def test_modify_group_name(app, db, groups):  # groups это имя файла с данными для создания и модификации групп
    if app.group_managment.check() is False:  # Проверяем есть ли хоть одна группа
        app.group_managment.Create_new_group(Group(name="12345"))  # Если нет, добавляем
    old_groups = db.get_group_list()  # длина группы до изменений
    index = randrange(len(old_groups))  # Создаем переменную с рандомным значением в пределах кол-ва групп
    groups.id = old_groups[index].id
    app.group_managment.modify_group_by_id(groups, groups.id)  # модифицируем группу с id, обявленным ранее
    new_groups = db.get_group_list()
    old_groups[index] = groups
    assert len(old_groups) == len(new_groups)  # Сравниваем длину до и после
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)  # Сортируем по ключу при сравнении
    #надо как-то заменить старую группу, содержащуюся в переменной groupr на новую groups





#def test_modify_group_header(app):
#    app.group_managment.modify_group(Group(header="Bomber"))


#def test_modify_group_footer(app):
#    app.group_managment.modify_group(Group(footer="Bomberman"))


#def test_modify_group_full(app):
#    app.group_managment.modify_group(Group(name="pups", header="pupus", footer="pupupus"))
