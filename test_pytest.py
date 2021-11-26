import pytest
import stringop

@pytest.fixture()
def before_test():
    print('----------------------before')
    yield
    print('----------------------after')

def test_concat(before_test):
    a = stringop.stgconcat('suraj', 'mazumdar')
    assert a ==  'surajmazumdar'
    print('----First')


def test_upper(before_test):
    a = stringop.uppercase('suraj')
    assert a ==  'SURAJ'
    print('----Second')