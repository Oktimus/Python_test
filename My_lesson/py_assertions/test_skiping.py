import sys
import pytest

pytestmark = pytest.mark.skipif(sys.platform != 'win32', reason=" OS is not allow version")

const = 9/5


def cent_to_fan(cent=0):
    fah = (cent * const) + 32
    return fah


print(cent_to_fan())

@pytest.mark.sanity
def test_case01():
    assert type(const) == float


#@pytest.mark.skipif(sys.version_info > (3, 6), reason=" Python is not allow version")
@pytest.mark.skipif(cent_to_fan() == 32, reason=" Error and bug")
def test_case02():
    assert cent_to_fan() == 32


def test_pase03():
    assert cent_to_fan(38) == 100.4
