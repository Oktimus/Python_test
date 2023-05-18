import pytest


@pytest.fixture()
def f_cfg_obj(request):
    """fixture: Получает данные перед выполнением тестовой функции"""
    print('>', 'fixture: Запуск f_set_obj()')
    marker = request.node.get_closest_marker('f_data')
    data = None if marker is None else marker.args[0]
    print('fixture:', data)
    return data.replace('Переданный', 'Измененый').replace('в', 'от')


@pytest.mark.f_data('Переданный параметр в fixture')
def test_1(f_cfg_obj):
    print('test1:', f_cfg_obj)
    assert True