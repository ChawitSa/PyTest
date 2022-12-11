from BMI import *
import pytest

@pytest.mark.parametrize('m,h,exp_res',
    [(55,75,"X3M Obese"),
    (55,76,"X3M Obese"),
    (55,194,"Underweight"),
    (55,195,"Underweight"),
    (55,170,"Nomal"),
    (5,170,"Underweight"),
    (6,170,"Underweight"),
    (109,170,"X3M Obese"),
    (110,170,"X3M Obese"),
    (70,170,"OVWeight"),
    (80,170,"Obese"),
    (55,74,"height under 75 [75,195]"),
    (55,196,"height over 195 [75,195]"),
    (4,170,"mass under 5 [5,110]"),
    (111,170,"mass over 110 [5,110]")])

def test_amount_two_input(m,h,exp_res):
    actual_result = over(m,h)
    assert exp_res == actual_result
