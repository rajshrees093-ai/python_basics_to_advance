pi =3.14159

def square(x):
    return x ** 2

def cube(x):
    return x**3

def circumference(radius):
    return 2* pi*radius

def area(radius):
    return pi*radius*radius

import create_module
result = create_module.area(3)
print(result)