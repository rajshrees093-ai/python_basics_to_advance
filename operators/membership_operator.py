# membership operator= used to test whether a value or variable is found in a sequence
#                         (string, list, tuple, set or dictionary)
#                         1. in
#                         2. not in

word="APPLE"

letter=input("guess a letter in the secret word: ")

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} was not found!")

#set
students={"raj", "rajat", "bob"}

student=input("enter name of a student: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")

#dictionary
grades={"Sandy":"A", "Squidward":"B", "Spongebob":"C", "Patrick":"D"}
student = input ("enter name of student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")
