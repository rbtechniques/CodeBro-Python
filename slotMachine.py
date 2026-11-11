import random


def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","⭐"]

    return [random.choice(symbols) for _ in range(3)]          #here I have used "_" instead of "symbols" in for because _ means it works for every value in given range and we have given symbols in random.choice so it will use it


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*2.5
        elif row[0]=='🍋':
            return bet*2
        elif row[0]=='🔔':
            return bet*1.5
        elif row[0]=='⭐':
            return bet*3.5
    return 0


def main():
    balance = 100

    print("Welcome to PySlots")
    print("Symbols: 🍒🍉🍋🔔⭐")
    while balance>0:
        print(f"Current Balance: ${balance}")

        bet = int(input("Enter your bet amount: "))

        if bet <0:
            print("Please enter a valid amount")
            continue 

        if bet>balance:
            print("Please stay in your limits!")
            continue
        if bet <= 0:
            print("Invalid Amount!")
            continue
        balance -= bet

        row = spin_row()
        print(row)

        payout = get_payout(row, bet)

        if payout>0:
            print(f"You Won ${payout}")
        else:
            print("Better Luck Next Time")

        balance += payout

        play_again = input("Do You Want To Play Again? (Y/N): ").upper()

        if play_again != "Y":
            break
    print("********************************************")
    print(f"Game Over! Your final balance is ${balance}")
    print("********************************************")




if __name__  == '__main__':
    main()