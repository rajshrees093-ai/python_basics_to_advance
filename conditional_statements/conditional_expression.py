# conditional expression = a one line shortcut for the if-else statement ie ternary operator
#                         print or assign one of two values based on a condition
#                         x if condition else y

num=5
a=6
b=7
age=22 
temp=30
user_role= "admin"

# print("positive" if num >0 else "negative")
# result= "even"  if num%2==0 else "odd"
# max_num= a if a>b else b
# print(max_num)

# min_num= a if a<b else b
# print(min_num)

# status = "adult" if age>=18 else "not adult"
# print(status)

# weather = "🥵" if temp>30 else "😎"
# print(weather)

access_level= "access granted" if user_role=="admin" else "limited acess"
print(access_level)