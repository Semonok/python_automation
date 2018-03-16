from model.group import Group
from selenium.common.exceptions import NoSuchElementException


def test_modify_group_name(app):
    try:
        app.group_managment.select_first_group()
    except NoSuchElementException:
        app.group_managment.Create_new_group(Group(name="123", header="321", footer="195"))
    finally:
        old_groups = app.group_managment.get_group_list()
        app.group_managment.modify_first_group(Group(name="Bomb"))
        new_groups = app.group_managment.get_group_list()
        assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    app.group_managment.modify_first_group(Group(header="Bomber"))


def test_modify_group_footer(app):
    app.group_managment.modify_first_group(Group(footer="Bomberman"))


def test_modify_group_full(app):
    app.group_managment.modify_first_group(Group(name="pups", header="pupus", footer="pupupus"))
