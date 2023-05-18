import pytest


@pytest.fixture()
def f_pre_return_obj_1():
    """fixture: Возвращает объект"""
    print('>> fixture: Запуск f_pre_return_obj_1()')
    return 'Объект из fixture 1'


@pytest.fixture()
def f_pre_return_obj_2():
    """fixture: Возвращает объект"""
    print('>> fixture: Запуск f_pre_return_obj_2()')
    return 'Объект из fixture 2'


@pytest.fixture()
def f_return_obj(f_pre_return_obj_1, f_pre_return_obj_2):
    """fixture: При вызове возвращает объект собранный из других fixture"""
    print('> fixture: Запуск f_return_obj()')
    return '{}, {}'.format(f_pre_return_obj_1, f_pre_return_obj_2)


def test_1(f_return_obj):
    data = f_return_obj
    print('test1: Объекты из f_return_obj() -', data)
    assert True
