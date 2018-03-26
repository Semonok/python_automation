import pytest
import json
import os.path
from fixture.application import Application

fixture = None
target = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    global target
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
    if target is None:
        with open(path_file) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=target["browser"], base_url=target["baseUrl"])
    fixture.session.login(username=target["username"], password=target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--target', action='store', default='target.json')