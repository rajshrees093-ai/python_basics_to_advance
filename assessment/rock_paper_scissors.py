import random

options=("rock", "paper", "scissors")
running=True
while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("enter your choice (rock, paper, scissors): ")
        print(f"player:{player}")
        print(f"computer:{computer}")

        if player == computer:
            print("it's a tie!")
        elif player =="rock" and computer =="scissors":
            print("you won!")
        elif player == "scissors" and computer =="paper":
            print("you won!")
        elif player =="paper" and computer =="rock":
            print("you won!")
        else:
            print("you lose!")
        
        play_again=input("play again? (y/n): ").lower()
        if not play_again == "y":
            running= False

print("thamks for playing!!")




