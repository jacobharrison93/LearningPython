def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def muliply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by 0')
    return x/y

print(add(5,10))