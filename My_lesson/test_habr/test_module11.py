import pytest

class BDVar:
    """Класс для хранения переменных"""
    def __init__(self, msg):
        self.var = msg

    def get_var(self):
        return self.var

    def set_var(self, new_var):
        self.var = new_var

@pytest.fixture(scope='class', autouse=True)
def f_wrapper_class(request):
    """fixture: Обертка для тестового класса, которая создает переменную"""
    print('>', 'fixture: Запуск обертки f_wrapper_class()')
    request.cls.var = BDVar('var: значение заданное fixture')
    yield
    print('>', 'fixture: Завершение обертки f_wrapper_class()')

@pytest.fixture()
def f_cfg_obj(request):
    """fixture: Получает объект из переменной класа перед выполнением тестовой функции"""
    print('>>', 'fixture: Запуск f_set_obj')
    print('fixture:', request.cls.var.get_var())
    request.cls.var.set_var('var: новое значение заданное в fixture')
    print('fixture:', request.cls.var.get_var())

class TestSuite:

    def test_1(self):
        print('TestSuite: Запуск test1')
        print(self.var.get_var())
        self.var.set_var('var: новое значение')
        print(self.var.get_var())
        assert True

    def test_2(self, f_cfg_obj):
        print('TestSuite: Запуск test2')
        f_cfg_obj
        print(self.var.get_var())
        assert True