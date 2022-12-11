import sys
sys.path.insert(0, './function')

from calculate import amount, validate_input, display_error
import pytest

@pytest.mark.parametrize('input01,input02,expected_result',[(1,3,4),(2,3,5),(2,-3,-1),(-2,-3,-5),(0.5,0.1,0.6),(5,0.1,5.1),(8,"","Input "+" again.."),("",8,"Input "+" again..")])

def test_amount_two_input(input01,input02,expected_result):
    actual_result = amount(input01,input02)
    assert expected_result == actual_result

@pytest.mark.parametrize('input,expected_result',[("",False)])
def test_false_validation_input_string(input,expected_result):
    actual_result = validate_input(input)
    assert expected_result == actual_result

@pytest.mark.parametrize('input,expected_result',[(1,True)])
def test_true_validate_input_number(input,expected_result):
    actual_result = validate_input(input)
    assert expected_result == actual_result

@pytest.mark.parametrize('index,expected_result',[("1","Input "+str(1)+" again..")])
def test_show_string_display_error_index1(index,expected_result):
    actual_result = display_error(index)
    assert expected_result == actual_result

@pytest.mark.parametrize('index,expected_result',[(2,"Input "+str(2)+" again..")])
def test_show_string_display_error_index2(index,expected_result):
    actual_result = display_error(index)
    assert expected_result == actual_result