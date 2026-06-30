# dictionary= a collection of {key:value} pairs
#             ordered and changeable, no duplicates for keys but values can be

capitals={"USA":"Washington D.C.", 
          "India": "New Delhi", 
          "Russia":"MOscow", 
          "China":"Beijing"}

#methods of dictionaries

print(capitals.get("USA"))
 
# if capitals.get("Japan"):
#     print("That capital doesnt exist")

capitals.update({"Germany": "Berlin"})
print(capitals)

capitals.update({"USA": "Detroit"})
print(capitals)

capitals.pop("China")
print(capitals)

capitals.popitem() #will remove the latest pair
print(capitals)

# capitals.clear() #clears the complete dictionary
# print(capitals)

keys=capitals.keys()
for key in capitals.keys():
    print(key)
print(keys)

values=capitals.values
for value in capitals.values():
    print(value)
print(values)

items = capitals.items() #items returns a dictionary object which resembles 2d list of tuples
for key, value in capitals.items():
    print(f"{key}: {value}")
