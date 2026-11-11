
def show_balance(balance):
    print("****************")
    print(f"Your balance is ${balance:.2f}")
    print("****************")

def deposit():
    print("****************")
    amount = float(input("Enter an amount to be deposited: "))
    print("****************")

    if amount<0:
        print("****************")
        print("This is not valid! Do you want to withdraw!!")
        print("****************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("****************")
    amount = float(input("Enter amount to be withdraw: "))
    print("****************")

    if amount>balance:
        print("****************")
        print(f"You can not withdraw greater than ${balance}")
        print("****************")
        return 0
    elif amount<0:
        print("****************")
        print("Amount must be greater than zero")
        print("****************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running == True:
        print("****************")
        print("Banking Program")
        print("****************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("****************")

        choice = input("Enter your Choice[1-4]")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("****************")
            print("That is not a valid choice")
            print("****************")

    print("****************")
    print("ThankYou! Have a nice Day!")
    print("****************")

if __name__ =='__main__':
    main()
        