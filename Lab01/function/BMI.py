def cm2m(h):
    return h/100

def cal(m,h):
    if m>=5 and m<=110 and m>=75 and m<=75:
        h = cm2m(h)
        return m/(h*h)
    else:
        return False

def level(bmi):
        if bmi>=30:
            return "X3M Obese"
        elif bmi>=25:
            return "Obese"
        elif bmi>=23:
            return "OVWeight"
        elif bmi>=18.5:
            return "Nomal"
        else:
            return "Underweight"

def over(m,h):
    if m<5:
        return "mass under 5 [5,110]"
    elif m>110:
        return "mass over 110 [5,110]"
    if h>195:
        return "height over 195 [75,195]"
    elif h<75:
        return "height under 75 [75,195]"
    else:  
        bmi = level(cal(m,h))
        return bmi