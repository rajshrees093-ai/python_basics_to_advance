import time


my_time=int(input("enter the desired time in seconds: "))

# for x in range (0, my_time):
#     print(x)
#     time.sleep(3)
# time.sleep(2) #after given time it will print automatically
# print("TIME'S UP!!")

for x in range(my_time, 0, -1):
    seconds= x%60
    minutes= int(x/60)%60
    hours= int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!!")