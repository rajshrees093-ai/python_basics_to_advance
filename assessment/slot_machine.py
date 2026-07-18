import random

def spin_row():
    symbols=["🍉", "🍋", "🍒", "🔔", "⭐"]
    # results=[]
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

    return[random.choice(symbols) for _ in range(3)] # by list comprehension method

def print_row(row):
    print("***********************")
    print(" | ".join(row))
    print("***********************")

def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0]== "🍒":
            return bet*3
        elif row[0]=="🍉":
            return bet*4
        elif row[0]=="🍋":
            return bet*5
        elif row[0]=="🔔":
            return bet*10
        elif row[0]=="⭐":
            return bet*25
    
    return 0
    

def main():
    balance=100

    print("***********************")
    print("Welcome to Python SLots")
    print("Symbols: 🍉🍋🍒🔔⭐")
    print("***********************")

    while balance >0:
        print(f"Current balance: ${balance}")
        bet=input("Place your bet amount: ")

        if  bet.isalpha():
            print("please enter a valid number ")
            continue #continue keyword will skip the current iteration of the loop
        
        bet=int(bet)
        if bet>balance:
            print("insufficient funds")
            continue

        if bet <=0:
            print("bet must be greater than zero")         
            continue
        
        balance-=bet
        
        row= spin_row() #this function will return a list
        print("Spinning....\n")
        print_row(row)

        payout=get_payout(row, bet)
        if payout>0:
            print(f"you won ${payout}")
        else:
            print("sorry you lost this round")

        balance +=payout

        play_again=input("do you want to play again? (y/n): ").upper()
        if play_again != "y":
            break

    print(f"Game over! Your final balance s ${balance}")

if __name__=='__main__':
    main()