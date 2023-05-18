#  Через отдельный объект внутри класса

import pytest


class Connect:
    """Класс для соединения"""

    def __init__(self, config):
        self.cfg = config
        self.status = 'Объект создан'

    def get_cfg(self):
        return self.cfg

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status


@pytest.fixture(scope='class')
def f_wrapper_class(request):
    """fixture: Обертка для тестового класса"""
    print('>', 'fixture: Запуск обертки f_wrapper_class()')
    print('- Создание объекта')
    request.cls.connect = Сonnect('Параметры соединения')
    print('- config (fixture):', request.cls.connect.get_cfg())
    print('- status (fixture):', request.cls.connect.get_status())
    request.cls.connect.set_status('Соединение установлено')
    print('- status (fixture):', request.cls.connect.get_status())
    yield
    request.cls.connect.set_status('Соединение разорвано')
    print('- status (fixture):', request.cls.connect.get_status())
    print('>', 'fixture: Завершение обертки f_wrapper_class()')


@pytest.mark.usefixtures('f_wrapper_class')
class TestSuite:

    def test_1(self):
        print('TestSuite: Запуск test1')
        print('- status (fun):', self.connect.get_status())
        self.connect.set_status('Работа выполнена')
        print('- status (fun):', self.connect.get_status())
        assert True

    def test_2(self):
        print('TestSuite: Запуск test2')
        print('\n- status (fun):', self.connect.get_status())
        self.connect.set_status('В работе возникла ошибка')
        print('- status (fun):', self.connect.get_status())
        assert False
