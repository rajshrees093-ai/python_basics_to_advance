# fruits=["apple", "orange", "banana", "coconut"]
# fruits=[fruit.upper() for fruit in fruits]

fruits=[fruit.upper() for fruit in["apple", "orange", "banana", "coconut"]]
print(fruits)
fruit_chars=[fruit[0] for fruit in fruits]
print(fruit_chars)


#using if in the syntax

numbers=[1, -2, 3, -4, 5, -6]
positive_nums=[num for num in numbers if num>=0]
negative_nums=[num for num in numbers if num<0]
even_nums=[num for num in numbers if num%2==0]
odd_nums=[num for num in numbers if num%2!=0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)


#grades

grades=[85, 42, 79, 98, 56, 61, 32]
passing_grades=[grade for grade in grades if grade>=50]
print(passing_grades)