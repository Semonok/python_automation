from model.group import Group


def test_add_group(app, db, groups):
    group = groups
    old_groups = db.get_group_list()  # длина группы до добавления
    app.group_managment.Create_new_group(group)  # добавляем группу
    new_groups = db.get_group_list()  # длина группы после добавления\
    # Создаем проверку элементов группы
    old_groups.append(group)  # Добавляем в старый список групп, новую группу (это нужно только для проверки)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)  # Сортируем по ключу при сравнении
