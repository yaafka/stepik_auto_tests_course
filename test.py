import pytest


# def test_succeed():
#     assert True

# @pytest.mark.xfail
# def test_not_succeed():
#     assert False


# @pytest.mark.skip
# def test_skipped():
#     assert False

@pytest.mark.xfail
@pytest.mark.parametrize('number', [
    '1','2','3','4','5','6'])
def test_check(number):
    assert number == '6'