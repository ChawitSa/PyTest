import sys
sys.path.insert(0, './function')

from calculate import amount, validate_input, display_error
import pytest

@pytest.mark.parametrize('input01,input02,expected_result',[(1,3,4)])

def test_amount_two_input(input01,input02,expected_result):
    actual_result = amount(input01,input02)
    assert expected_result == actual_result