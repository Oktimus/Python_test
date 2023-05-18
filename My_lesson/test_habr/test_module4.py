import pytest


@pytest.fixture(scope='class', autouse=True)
def f_wrapper_class(request):
    """fixture: Обертка для тестового класса, которая также создает переменную"""
    print('>', 'fixture: Запуск обертки f_wrapper_class()')
    request.cls.var1 = 'var1: значение заданное fixture'
    yield
    print('>', 'fixture: Завершение обертки f_wrapper_class()')


@pytest.fixture(scope='class')
def f_set_var_in_class(request):
    """fixture: Задает тестовому классу переменную"""
    print('>> fixture: Запуск f_set_var_in_class()')
    request.cls.var2 = 'var2: значение заданное fixture'


@pytest.mark.usefixtures('f_set_var_in_class')
class TestSuite:

    def test_1(self):
        print('TestSuite: Запуск test1')
        print('{}\n{}'.format(self.var1, self.var2))
        self.var1 = 'var1: новое значение'
        self.var2 = 'var2: новое значение'
        print('{}\n{}'.format(self.var1, self.var2))
        self.var1 =' hhsdsdgsdgfsd'
        assert True

    def test_2(self):
        print('TestSuite: Запуск test2')
        print('{}\n{}'.format(self.var1, self.var2))
        assert True
