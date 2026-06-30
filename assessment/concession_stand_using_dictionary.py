menu = {"coldcoffee": 3.00, 
        "pizza": 5.00,
        "popcorn":4.00,
        "fries":3.00,
        "nachos": 3.50,
        "soda": 2.50,
        "lemonade": 2.75}

cart=[]
total=0

print("----------MENU---------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")

while True:
    food=input("select an item (q to quit): ")
    if food.lower()== "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR ORDER------")
for food in cart:
    total+=menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
