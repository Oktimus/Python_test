# через метод внутри фикстуры с использованием addfinalizer

import pytest


@pytest.fixture(scope='function')
def f_return_obj(request):
    """fixture: Возвращает объект"""
    print('>', 'fixture: Запуск f_return_obj()')
    print('- Создание объекта в fixture')
    data = 'Объект из fixture'
    # Функция корректного завершения объекта

    def del_object():
        print('- Завершение созданного объекта:', data)
        # Финализация
    request.addfinalizer(del_object)
    return data


def test_1(f_return_obj):
    print('TestSuite: Запуск test1')
    print('-', f_return_obj)
    assert True


def test_2(f_return_obj):
    print('TestSuite: Запуск test2')
    print('-', f_return_obj)
    assert False
