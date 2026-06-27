temp=float(input("enter temperature: "))
unit=input("celsius or farheneit? (c/f):")

if unit=="c":
    temp= (temp(9/5)+32)
    unit="f"
elif unit=="f":
    temp=(temp-32)*(5/9)
    unit="c"
else:
    print(f"{unit} was not valid")

print(f"so, temperature is: {round(temp, 2)} {unit}")