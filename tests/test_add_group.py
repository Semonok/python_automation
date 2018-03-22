from model.group import Group
import pytest
import random
import string

def random_string(maxlen):
    symbols = string.digits + string.ascii_letters + string.punctuation + ' '
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_string(10)]
    for header in ['', random_string(10)]
    for footer in ['', random_string(10)]]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group_managment.get_group_list()  # длина группы до добавления
    app.group_managment.Create_new_group(group)  # добавляем группу
    new_groups = app.group_managment.get_group_list()  # длина группы после добавления
    assert len(old_groups) + 1 == len(new_groups)  # сравниваем кол-во групп до и после добавления группы
    # Создаем проверку элементов группы
    old_groups.append(group)  # Добавляем в старый список групп, новую группу (это нужно только для проверки)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)  # Сортируем по ключу при сравнении
