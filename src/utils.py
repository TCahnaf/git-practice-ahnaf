def add(a,b):
    if type(a) != int or type(b) != int:
        return 'Sorry but both inputs must be integers'
    return a+b

def subtract(a,b):
    if type(a) != int or type(b) != int:
        return 'Sorry but both inputs must be integers'
    return a-b

def multiply(a,b):
    if type(a) != int or type(b) != int:
        return 'Sorry but both inputs must be integers'
    return a*b

def divide(a,b):
    if type(a) != int or type(b) != int:
        return 'Sorry but both inputs must be integers'
    if b == 0:
        ZeroDivisionError('Error when dividing by zero')

    return a//b
    


