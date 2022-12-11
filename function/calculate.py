def amount(a,b):
    if isinstance(a, str):
        return "Input Num1 again.."
    if isinstance(b,str):
        return "Input Num2 again.."
    return a+b

def display_error(index):
    return "Input "+str(index)+" again.."

def validate_input(num):
    if isinstance(num, str):
        return False
    return True