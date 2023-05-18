import pytest


@pytest.fixture(scope='module', autouse=True)
def f_wrapper_module():
    """ fixture: Обертка для тестового модуля"""
    print('>', 'fixture: Запуск обертки для тестовго модуля')
    yield
    print('>', 'fixture: Завершение обертки для тестовго модуля')


@pytest.fixture(scope='class', autouse=True)
def f_wrapper_class():
    """fixture: Обертка для тестового класса"""
    print('>>', 'fixture: Запуск обертки для тестовго класса')
    yield
    print('>>', 'fixture: Завершение обертки для тестовго класса')


@pytest.fixture(scope='function', autouse=True)
def f_wrapper_function():
    """fixture: Обертка для тестовой сессии"""
    print('>>>', 'fixture: Запуск обертки для тестовой функции')
    yield
    print('>>>', 'fixture: Завершение обертки для тестовой функции')


class TestSuite1:
    """Первый testsuite"""

    def test_1(self):
        print('TestSuite1: Запуск test1')
        assert True

    def test_2(self):
        print('TestSuite1: Запуск test2')
        assert True


class TestSuite2:
    """Второй testsuite"""

    def test_1(self):
        print('TestSuite2: Запуск test1')
        assert True

    def test_2(self):
        print('TestSuite2: Запуск test2')
        assert True
