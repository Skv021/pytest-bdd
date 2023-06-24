"""The dummy feature feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from src.tests.pages.login_page import Loginpage


@scenario('../features/login.feature', 'Its a dummy scenario')
def test_its_a_dummy_scenario():
    pass


global l


@given('I login app')
def _(driver):
    global l
    l = Loginpage(driver)


@when('I click on Submit')
def _():
    l.click_submit()


@when('I enter password')
def _():
    l.enter_password()


@when('I enter username')
def _():
    l.enter_username()


@then('I should be logged in')
def _():
    pass

@then('I pass 5 as arg')
def _():
    print("arg")
