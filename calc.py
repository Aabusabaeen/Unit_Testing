

def add(x,y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Substract Function"""
    return x - y

def multiply(x,y):
    """Multiply Function"""
    return x * y

def divide(x,y):
    """Divide Function"""
    if y == 0:
        raise ValueError('cannot devide by zero')

    return x / y
