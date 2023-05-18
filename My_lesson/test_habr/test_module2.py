import pytest


@pytest.fixture()
def f_return_obj():
    '''fixture: Возвращает объект'''
    print('> fixture: Запуск f_return_obj()')
    return 'объект из fixture'


def test_1(f_return_obj):
    data = f_return_obj
    print('test1: Объект из f_return_obj() -', data)
    assert True


def test_2(f_return_obj):
    data = f_return_obj
    print('test2: Объект из f_return_obj() -', data)
    assert True
