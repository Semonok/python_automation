from model.group import Group
import random


def test_del_group(app, db):
    if len(db.get_group_list()) == 0:  # Проверяем есть ли хоть одна группа
        app.group_managment.Create_new_group(Group(name="12345"))  # Если нет, добавляем
    old_groups = db.get_group_list()  # длина группы до удаления
    group = random.choice(old_groups)
    app.group_managment.delete_group_by_id(group.id)  # Удаляем группу с индексом, равным ранее полученной переменной
    new_groups = db.get_group_list()  # длина группы после удаления
    # Создаем проверку элементов группы
    old_groups.remove(group)
    assert old_groups == new_groups
