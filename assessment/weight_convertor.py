weight=float(input("enter weight:"))
unit=input("kilograms/pounds? (k/l):")

if unit == "k":
    weight= weight * 2.205
    unit="lbs"
elif unit == "l":
    weight=weight/2.205
    unit="kg"
else:
    print(f"{unit} was not valid")

print(f"your weight is: {round(weight, 2)}{unit}")