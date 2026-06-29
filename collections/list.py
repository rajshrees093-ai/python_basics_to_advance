fruits = ["apple", "mango", "banana", "guava"]
print(fruits)
print(fruits[0])
print(fruits[3])
print(fruits[::2])
print(dir(fruits))  
print(len(fruits ))
#dir function = The dir() function in Python is a built-in tool used for introspection, returning a list of valid attributes, methods, and names associated with an object or the current local scope.  
#                It is primarily used to explore unfamiliar modules, inspect class structures, and debug code by revealing available properties without needing to access their values. 
#print(help(fruits))  help fun = gives description of all the methods and attributes

#for x in fruits:  #used for iteration purpose    #x works as a counter ie an iterator
#   print(x)

fruits[0]="pineapple"
for x in fruits:
    print(x)


#methods in a list

fruits.append("orange") #append func is used to add the new element at the end of the list
print(fruits)

fruits.remove("banana") #remove func is used to remove that particular element\
print(fruits)

fruits.insert(0, "pear") #insert func is used to add element at any specific position
print(fruits)

fruits.sort() #sort func is used to sort the list
print(fruits)

fruits.reverse() #reverse func is used to reverdse the list
print(fruits)

#fruits.clear() #clear func clears the complete list
#print(fruits)


f1=fruits.index("orange") #index func is used to return the index value of the given element
print(f1)

f2=fruits.count("banana") #count func returns the count of that element
print(f2)