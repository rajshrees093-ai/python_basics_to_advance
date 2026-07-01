import random

lowest_num=1
highest_num=99
result= random.randint(lowest_num, highest_num)
guesses=0
is_running= True #once the user wins the game it will be set to false

print("python number guessing game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:

    guess=input("enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess < lowest_num or guess > highest_num:
            print("that number is out of range")
            print(f"please select a number between {lowest_num} and {highest_num} ")
        elif guess < result:
            print("too low! try again!")
        elif guess > result:
            print("too high!, try again!")
        else:
            print(f"COORECT! YOU GOT THE ANSWER AS {result}")
            print(f"number of guesses: {guesses}")
            is_running=False

    else:
        print("invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num} ")