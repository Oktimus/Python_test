import pytest


class BDVar:
    """Класс для хранения переменных"""

    def __init__(self, msg):
        self.var = msg

    def get_var(self):
        return self.var

    def set_var(self, new_var):
        self.var = new_var


@pytest.fixture(scope='class')
def f_wrapper_class(request):
    """fixture: Обертка для тестового класса, которая создает переменную"""
    print('>', 'fixture: Запуск обертки f_wrapper_class()')
    request.cls.var = BDVar('var: значение заданное fixture')
    yield
    print('>', 'fixture: Завершение обертки f_wrapper_class()')


@pytest.mark.usefixtures('f_wrapper_class')
class TestSuite:

    def test_1(self):
        print('TestSuite: Запуск test1')
        print(self.var.get_var())
        self.var.set_var('var: новое значение')
        print(self.var.get_var())
        assert True

    def test_2(self):
        print('TestSuite: Запуск test2')
        print(self.var.get_var())
        assert True