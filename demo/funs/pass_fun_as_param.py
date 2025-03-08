def add(a, b):
    return a + b

def mul(a, b):
    return a * b


def math_operation(operation, x, y):
    print(operation(x, y))


math_operation(add, 10, 20)
math_operation(mul, 10, 20)
#math_operation(int, "123")



