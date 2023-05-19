import pytest


pytestmark = [pytest.mark.smoke]

def test_case01():
    with pytest.raises(ZeroDivisionError):
        print('ff')
        assert (1/0)

def func1():
    raise ValueError("AAA")


@pytest.mark.xfail
def test_case02():
    with pytest.raises(Exception) as exinfo:
        #assert (1, 2, 3) == (1, 2, 4)
        func1()
    print(str(exinfo))
    assert str(exinfo.value) == 'AAA'


@pytest.mark.xfail(False, reason="dddddddddddddd")
def test_a3():
    assert "abc" == "advd"


@pytest.mark.xfail(raises=IndexError, reason="Index Errors")
def test_a4():
    letters = "sdbsdbfbsdfsd"
    assert letters[100]