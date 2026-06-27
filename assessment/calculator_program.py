operator= input("choose operator (+ - * /): ")

a=float(input("enter 1st number: "))
b=float(input("enter 2nd number: "))

if operator=="+":
    res=a+b
    print(f"the sum is: {res}")

elif operator=="-":
    res=a-b
    print(f"the difference is:{res}")

elif operator=="*":
    res=a*b
    print(f"the product is: {res}")

elif operator=="/":
    res=a/b
    print(f"divison is: {res}")

else:
    print("enter valid operator")

