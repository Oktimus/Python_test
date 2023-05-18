import pytest


@pytest.fixture()
def f_cfg_obj(request):
    """fixture: Через метод возвращает объект"""
    print('>', 'fixture: Запуск f_set_obj()')

    def _set_cfg(cfg):
        print('>>', 'fixture: Запуск _set_cfg()')
        return cfg.replace('переданный в', 'измененый от')

    return _set_cfg


def test_1(f_cfg_obj):
    data_1 = f_cfg_obj('переданный в fixture параметр-1')
    data_2 = f_cfg_obj('переданный в fixture параметр-2')
    print('test1:\n- {}\n- {}'.format(data_1, data_2))
    assert True
