import pytest


class BDVar:
    """Класс для хранения переменных"""

    def __init__(self, msg):
        self.var = msg

    def get_var(self):
        return self.var

    def set_var(self, new_var):
        self.var = new_var


var = BDVar('var: значение по умолчанию')


@pytest.fixture(scope='class')
def f_wrapper_class():
    """fixture: Обертка для тестового класса, которая создает переменную"""
    print('>', 'fixture: Запуск обертки f_wrapper_class()')
    print(var.get_var())
    var.set_var('var: значение заданное fixture')
    print(var.get_var())
    yield
    print('>', 'fixture: Завершение обертки f_wrapper_class()')


@pytest.mark.usefixtures('f_wrapper_class')
class TestSuite:

    def test_1(self):
        print('TestSuite: Запуск test1')
        print(var.get_var())
        var.set_var('var: новое значение')
        print(var.get_var())
        assert True

    def test_2(self):
        print('TestSuite: Запуск test2')
        print(var.get_var())
        assert True
