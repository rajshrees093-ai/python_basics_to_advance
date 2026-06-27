#logical operator= evaluate multiple condition (or, and, not)
#                     or= atleast one condition must be true
#                     and=both condition must be True
#                     not inverts the condition (not false, not true)

temp= 36 
is_raining= False

if temp>35 or temp< 0 or is_raining:
    print("the outdoor event is cancelled")
else:
    print("the outdoor event is still scheduled")

                  