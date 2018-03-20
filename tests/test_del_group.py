from model.group import Group
from random import randrange


def test_del_group(app):
    if app.group_managment.check() is False:  # Проверяем есть ли хоть одна группа
        app.group_managment.Create_new_group(Group(name="12345"))  # Если нет, добавляем
    old_groups = app.group_managment.get_group_list()  # длина группы до удаления
    index = randrange(len(old_groups))  # Создаем переменную с рандомным значением в пределах кол-ва групп
    app.group_managment.delete_group(index)  # Удаляем группу с индексом, равным ранее полученной переменной
    new_groups = app.group_managment.get_group_list()  # длина группы после удаления
    assert len(old_groups) - 1 == len(new_groups)  # Сравниваем кол-во групп до и после удаления
    # Создаем проверку элементов группы
    del old_groups[index]
    assert old_groups == new_groups
