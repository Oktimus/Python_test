import pytest


@pytest.fixture()
def f_wrapper_function():
    """fixture: Обертка для тестовой функции, которая возвращает объект"""
    print('>', 'fixture: Запуск обертки f_wrapper_function()')
    print('- Создание объекта в fixture')
    data = 'Объект из fixture'
    yield data
    print('- Завершение созданного объекта:', data)
    print('>', 'fixture: Завершение обертки f_wrapper_function()')


def test_1(f_wrapper_function):
    print('TestSuite: Запуск test1')
    print('-', f_wrapper_function)
    assert True


def test_2(f_wrapper_function):
    print('TestSuite: Запуск test2')
    print('-', f_wrapper_function)
    assert False