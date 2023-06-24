import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--username", action="store", default="default name")
    parser.addoption("--password", action="store", default="default name")


def pytest_configure(config):
    os.environ["username"] = config.getoption("username")


@pytest.fixture
def get_pass(request):
    password = request.config.getoption("password")
    return password
