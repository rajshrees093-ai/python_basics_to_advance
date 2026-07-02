# *args= allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#             *unpacking operator

def add(*args): #parameter name can vary
    # print(type(args))
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1, 2, 3,9))