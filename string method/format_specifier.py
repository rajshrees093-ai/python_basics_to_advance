# format specifier= {:flags} format a value based on what flags are inserted

# .(number)f= round to that many decimal places (fixed point)
# :(number)= allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :<= left justify
# :> = right justify
# :^ =center align
# :+ = use a plus sign to indicate positive Value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1= 3000.14159
price2= -9755.36
price3= 1280.56

# print(f"price 1 is {price1:.2f}") #f is floating point number
# print(f"price 2 is {price2:.3f}")
# print(f"price 3 is {price3:.2f}")

print(f"price 1 is ${price1:+,.2f}") 
print(f"price 2 is ${price2:+,.3f}")
print(f"price 3 is ${price3:+,.2f}")

