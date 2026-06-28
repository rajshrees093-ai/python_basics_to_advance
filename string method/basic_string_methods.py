name= input("enter your name: ")
result=len(name) #used to return or find the length or the no. of characters the string holds
print(result)
phone_number=input("enter your phone number #: ")

result=name.find(" ") #used to find first occurence of the character
print(result)

result=name.rfind("e") #used to find the last occurence of the character
print(result)

name=name.capitalize() #it capitalize the first alphabet
print(name)

name=name.upper() #it makes all the character of string in upper case
print(name) 

name=name.lower() #it makes all the character of string in lower case
print(name) 

result=name.isdigit() #check whether the string contains digit or not if yes returns true else false
print(result)

result=name.isalpha() #check whether the string contains alphabet or not if yes returns true else false
print(result)

res=phone_number.count("-") #counts the number of occurence of a particular character in the string
print(res)

phone_number=phone_number.replace("-", " ")
print(phone_number)





