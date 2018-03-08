import pytest
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test(app):
    app.session.Login(username="admin", password="secret")
    app.session.Logout()