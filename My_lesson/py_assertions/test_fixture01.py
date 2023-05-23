import pytest


@pytest.fixture()
def setup_list():
    print("\n in fixtures.. \n")
    city = ["aaa", "bbb", "ccc", "dddd", "eee"]
    yield city


def test_case01(setup_list):
    print(f"aaaaaaaaaaaaa     {setup_list}")


@pytest.mark.usefixtures("setup_list")
def test_case03():
    print(setup_list)
    assert True
