from selenium.common.exceptions import NoSuchElementException
from model.group import Group


def test_del_group(app):
    try:
        app.group_managment.select_first_group()
    except NoSuchElementException:
        app.group_managment.Create_new_group(Group(name="123", header="321", footer="195"))
    finally:
        app.group_managment.delete_group()


