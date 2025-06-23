#python slots gaming
import random

def spin_row():
    symbols = ['🍊', '🍉', '🔔', '🍋', '🫐']
    return [random.choice(symbols) for _ in range(3)]       #random choices for 3 symbols

def print_row(row):                                         #printing the symbols                            #
    print(" | ".join(row))
def get_payout(row , bet ):                                 #payout if user wins the function
    if row[0]==row[1]==row[2]:
        if row[0]=='🍊':
            return bet*2
        elif row[0]=='🍉':
            return bet*3
        elif row[0]=='🔔':
            return bet*5
        elif row[0]=='🍋':
            return bet*10
        elif row[0]=='🫐':
            return bet*20
    return 0
def main():
    balance = 100
    print("************************")
    print("Welcome to python slots ")
    print("Symbols: 🍊 🍉 🔔 🍋 🫐")
    print("************************")
    while balance >0:
        print(f"Your available balance is ${balance}")
        print("*************************************")
        bet = input("Place you bet: ")

        if not bet.isdigit():
            print("****************************")
            print("Bet must be in numbers only ")
            print("****************************")
            continue

        bet = int(bet)
        if bet > balance:
            print("*******************")
            print("Insufficient Funds!")
            print("*******************")
            continue

        if bet <=0:
            print("**************************")
            print("Bet must be greater than 0")
            print("**************************")
            continue

        balance-=bet

        row = spin_row()
        print_row(row)
        payout = get_payout(row , bet)
        if payout>0:
            print("******************************")
            print(f"You won this round! ${payout}")
            print("******************************")
        else:
            print("********************")
            print("You lose this round!")
            print("********************")

        balance+=payout

        play_again = input("Do you want to play again(Y/N) : ").upper()
        if play_again != 'Y':
            break
    print(f"Game Over! your final balance ${balance}")
if __name__ == '__main__':
    main()