#we are using list here cuz tuples cant be modified and sets are unordered
foods = []
prices= []
total= 0 

while True:
    food= input("enter a food to buy (q to quit): ")
    #if food.lower()=="q" incase somebody types in capital Q
    if food=="q":
        break
    else:
        price=float(input(f"enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("------------YOUR CART-----------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total=total+price

print()
print(f"your total bill is: ${total}")