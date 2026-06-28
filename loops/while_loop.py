#while loop= execute some code WHILE some condition remains true

name = input("enter your name: ")
# if name == "":
#     print("you didnot enter your name")
# else:
#     print(f"hello {name}")

while name == "":
    print("you did not enter your name")
    name= input("enter your name: ")

print(f"hello {name}")


age=int(input("enter your age: "))
while age<0:
    print("age cant be negative")
    age=int(input("enter your age: "))
print(f"you are {age} years old")


food= input("enter a food you like (q for quit): ")

while not food=="q":
    print(f"you like {food}")
    food= input("enter another food you like (q for quit): ")
print("bye")


num= int(input("enter a number between 1-10: "))
while num<1 or num>10:
    print(f"{num} is invalid")
    num=int(input("enter a number between 1-10: "))
print(f"your number is {num}")
