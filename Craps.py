# Temur Khabibullaev
# 10/21/2019
import random
import time

print('ENTER your balance:')
balance = int(input('> '))
print("Good! Let's start! Place how much you bet!")
bet = int(input('> '))
total_amount = balance - bet


def start():
    # Balance
    print('''
    Welcome to Craps Game!
    The Dice will be rolled!''')
    total_amount = balance - bet
    while bet > total_amount:
        rollDice()
        game()


def finish():
    print('Good Job! Game is finished. Here is your balance:\n> ', total_amount)


def rollDice():
    points = random.randint(2,12)
    return points


def win():
    won_money = total_amount + bet * 2
    print('Wow! You won! Your win is: ',won_money)


def loosing():
    lost_money = total_amount - bet * 2
    print('You lose. This is your lose amount:', lost_money)


def game():
    roll = rollDice()
    print('Your dice: ', roll)
    if int(roll) == 7 or int(roll) == 11:
        time.sleep(3)
        win()
    elif int(roll) == 2 or int(roll) == 3 or int(roll) == 12:
        time.sleep(3)
        loosing()
    elif roll == 4 or roll == 5 or roll == 6 or roll == 8 or roll == 9 or roll == 10:
        print(f'Your points: {roll}. You will keep rolling until you get same points (Win) or 7 (Lose).')
        print('This is your balance now: ',total_amount)
        new_roll = random.randint(2,12)
        while roll != new_roll and new_roll != 7:
            print(f"You have rolled a {new_roll}, we'll keep going.")
            time.sleep(2)
            new_roll = random.randint(2,12)
        if new_roll == roll:
            print(f"You got {new_roll}!")
            win()
        elif new_roll == 7:
            print(f"You got {new_roll}")
            loosing()
    decision = input('Are we playing? Know - wins or loses will be cut from your balance. Enter an INTEGER only:\n1) Yes\n2) No\n> ')
    if int(decision) == 1:
        start()
    elif int(decision) != 1:
        print('Good Luck! See you next time.')
        finish()


start()