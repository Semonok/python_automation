from selenium.common.exceptions import NoSuchElementException
from model.group import Group


def test_del_group(app):
    try:
        app.group_managment.select_first_group()
    except NoSuchElementException:
        app.group_managment.Create_new_group(Group(name="123", header="321", footer="195"))
    finally:
        old_groups = app.group_managment.get_group_list()  # длина группы до удаления
        app.group_managment.delete_group()
        new_groups = app.group_managment.get_group_list()  # длина группы после удаления
        assert len(old_groups) - 1 == len(new_groups)
        old_groups[0:1] = []
        assert old_groups == new_groups



