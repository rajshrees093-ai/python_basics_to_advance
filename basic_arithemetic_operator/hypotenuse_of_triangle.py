import math

l=float(input("enter the length of the triangle:"))
b=float(input("enter breadth:"))

# lb= (pow(l,2)+pow(b,2))
# hypotenuse=pow(lb, 1/2)
hypotenuse=math.sqrt(pow(l,2)+pow(b,2))

print(f"the hypotenuse of the triangle is: {hypotenuse}")