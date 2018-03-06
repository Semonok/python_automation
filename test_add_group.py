import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.Login(username="admin", password="secret")
    app.Create_new_group(Group(name="123", header="321", footer="195"))
    app.Logout()

