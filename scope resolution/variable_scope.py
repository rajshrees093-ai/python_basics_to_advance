# variable scope= where a variable is visible and accessible
#scope resolution = (LEGB) Local -> enclosed -> global -> built-in

# def func1(): #variable declared inside a function has a local scope
#     a=1  #here a is the local variable for func1
#     print(a)

# def func2():
#     b=2 #here b is the local variable for func2
#     print(b)

# func1()
# func2()

from math import e
def func1():
    print(e)  #biuilt-in scope
func1()


