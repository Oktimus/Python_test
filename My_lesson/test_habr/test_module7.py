import pytest


@pytest.fixture(params=['параметр 1', 'параметр 2'])
def f_wrapper_function(request):
    """fixture: Возвращает объект"""
    print('>', 'fixture: Запуск обертки f_wrapper_function()')
    print('fixture: Создание объекта')
    data = f'Объект из fixture: {request.param}'
    yield data
    print('fixture: Завершение созданного объекта')
    print('>', 'fixture: Завершение обертки f_wrapper_function()')


def test_1(f_wrapper_function):
    print('TestSuite: Запуск test1')
    print(f_wrapper_function)
    assert True


def test_2(f_wrapper_function):
    print('TestSuite: Запуск test2')
    print(f_wrapper_function)
    assert True