#logical operator= evaluate multiple condition (or, and, not)
#                     or= atleast one condition must be true
#                     and=both condition must be True
#                     not inverts the condition (not false, not true)

# temp= 36 
# is_raining= False

# if temp>35 or temp< 0 or is_raining:
#     print("the outdoor event is cancelled")
# else:
#     print("the outdoor event is still scheduled")

temp =25
is_sunny = True

if temp>=28 and is_sunny:
    print("it is hot outside🥵")
    print("it is sunnyyyyy☀️")
elif temp<=0 and is_sunny:
    print("it is cold today🥶")
    print("it is sunnyyy☀️")
elif 28>temp and is_sunny:
    print("it is warm outside🫠")
    print("it is sunnyyy☀️")
elif temp<=0 and not is_sunny:
    print("it is cold outside🥶")
    print("it is cloudyy💭")