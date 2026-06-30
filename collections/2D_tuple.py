# fruits=("apple", "mango","pear", "orange")
# vegetables=("potato","onion","tomato", "capsicum")
# meat=("chicken", "fish","lamb")

# groceries=(fruits, vegetables, meat)
# print(groceries)
# print(groceries[0][1]) #accessing index of elements in 2d matrix

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

num_pad=((1,2,3),
        (4,5,6),
        (7,8,9),
        ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()