import pytest


def test_case01():
    with pytest.raises(ZeroDivisionError):
        print('ff')
        assert (1/0)

def func1():
    raise ValueError("AAA")


def test_case02():
    with pytest.raises(Exception) as exinfo:
        #assert (1, 2, 3) == (1, 2, 4)
        func1()
    print(str(exinfo))
    assert str(exinfo.value) == 'AAA'