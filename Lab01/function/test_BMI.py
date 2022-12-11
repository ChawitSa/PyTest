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

def test_level(m,h,exp_res):
    actual_result = over(m,h)
    assert exp_res == actual_result

@pytest.mark.parametrize('m,h,exp_res',
    [(55,75,97.78),
    (55,76,95.22),
    (55,194,14.61),
    (55,195,14.46),
    (55,170,19.03),
    (5,170,1.73),
    (6,170,2.08),
    (109,170,37.72),
    (110,170,38.06),
    (70,170,False),
    (80,170,False),
    (55,74,False),
    (55,196,False),
    (4,170,False),
    (111,170,False)])
def test_bmi(m,h):
    actual_result = cal(m,h)
    assert exp_res == actual_result