def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    print("*********************")
    amount=float(input("enter the amount to be deposited: "))
    print("*********************")
    if amount<0:
        print("not a valid amout")
    else:
        return amount

def withdraw(balance):
    print("*********************")
    amount=float(input("enter amount to be withdrawn: "))
    print("*********************")

    if amount>balance:
        print("Insufficient bank balance ")
    elif amount<0:
        print("amount must be greater than zero")
        return 0
    else:
        return amount
    
def main():

    balance=0
    is_running=True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        choice= input("enter your choice (1-4): ")

        if choice=="1":
            show_balance(balance)

        elif choice=="2":
            balance += deposit()

        elif choice =="3":
            balance-= withdraw(balance)
        
        elif choice=="4":
            is_running=False
        
        else:
            print("*********************")
            print("invalid!")
            print("*********************")

    print("*********************")
    print("Thank You! Have a nice day!")
    print("*********************")

if __name__=='__main__':
    main()