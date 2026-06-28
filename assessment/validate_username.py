#validate user input exercise
# 1. usrname is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username=input("enter your username: ")
 
if len(username)<=12 and username!=" " and username.isdigit()==False:
    print("this is a valid username!")
else:
    print("check your username")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
# if len(username) > 12:
#     print("username cant be more than 12 characters")
# elif not username.find(" ")==-1:
#     print("username cant contain spaces")
# elif not username.isalpha():
#     print("username cant contain numbers")
# else:
#     print(f"welcome {username}")