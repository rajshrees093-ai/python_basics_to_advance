cars = {"porsche", "range rover", "thar", "mesarati", "defender"}
print(cars)
print("maruti" in cars) #returns true or false based on the availability of element
#print(cars[1])  indexing isnt allowed as sets are unordered


#methods used in sets

cars.add("ferrari") #adds the element in the set
print(cars)

cars.pop() #randomly remove/pop thefirst element that appears first in a set 
print(cars)

cars.clear() #clears the whole set

