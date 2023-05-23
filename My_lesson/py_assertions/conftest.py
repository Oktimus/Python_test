import pytest

QA_config = 'qa.prop'
prod_config = 'prod.prop'


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default='QA')


@pytest.fixture
def CmdOpt(pytestconfig):
    print(" \n In CmdOpt  fixture ")
    opt = pytestconfig.getoption("cmdopt")
    if opt == 'prod':
        f = open(prod_config, 'r')
    else:
        f = open(QA_config, 'r')
    yield f




