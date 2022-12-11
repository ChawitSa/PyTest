def amount(a,b):
    if not validate_input(a):
        return display_error(a)
    if not validate_input(b):
        return display_error(b)
    return a+b

def display_error(index):
    return "Input "+str(index)+" again.."

def validate_input(num):
    if isinstance(num, str):
        return False
    return True
