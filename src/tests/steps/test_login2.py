"""The dummy feature feature tests."""

from pytest_bdd import (
    given,
    scenario,
    parsers,
    then,
    when,
)


@scenario('../features/login2.feature', 'Its a dummy scenario3')
def test_its_a_dummy_scenario3():
    pass


@given(parsers.cfparse('I have "{prm}" apples'))
def _(prm):
    print("+++++++++++",str(prm))
    print(type(prm))

@then(parsers.cfparse('I enter username as "{username}"'))
def x(username):
    print("my username :",username)
    print(type(username))