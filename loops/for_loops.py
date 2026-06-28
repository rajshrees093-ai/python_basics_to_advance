# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc


# for x in range (1,11):  #basic sytnax
#     print(x)
# print("happy new year")

# for x in reversed(range(1,11)):
#     print(x)
# print("hi") 

# credit_card="1234-7890-6565-2479"
# for y in credit_card:
#     print(y)

for x in range (1,21):
    if x==13:
        continue #skips the number and continues to last iteration
    else:
        print(x)

for y in range (1,15):
    if y==10:
        break #if the condition becomes true and then there is break condition it will skip the loop and stop printing
    else:
        print(y)