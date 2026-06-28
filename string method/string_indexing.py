#indexing = accessing elements ofa sequence using [] (indexing operator)
#         [start:end:step]

credit_number= "1234-5678-0987-3579"

print(credit_number[13]) #if indexing is given only in single value then it is by default taken as the start value
print(credit_number[0:4]) #last/end index is exclusive that is indexing is always done till end-1 and starting index is inclusive
print(credit_number[:4]) # if not given the starting index then by default it is taken as the start/beginning index value
print(credit_number[5:9])
print(credit_number[5: ]) #if not given end value then everything is printed till the last character of the string
print(credit_number[-1]) #-ve index prints the last character of the string
print(credit_number[::2]) #characters will be printed from beginning to end at the step of 2

last_digits=credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

credit_number= credit_number[::-1] #-ve step allows the string to print backwards
print(credit_number)
