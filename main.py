import random

print("Welcome to the game of dice!")
print("You start with 100 point you have to think of a number 2,12 and make a bet, the computer will roll a 2 dice")
print("If the number you thought of is under 7 and the dice gave you a number under 7 then you win.")
print("Same thing with over 7.")
print("If you guess the exact number that the dice rolls then you win 4X the points than usual.")
print("If none of that happens then you win nothing and lose your bet.")

points = 100

while points > 0:
    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    sum = number1 + number2
    user_number = int(input("Number -> "))
    user_bet = int(input("Bet -> "))

    if sum == user_number:
        print("Because you guessed the exact number you win 4X of your bet!")
        points = points + user_bet * 4
    elif sum <= 7 and user_number <= 7:
        print("You won!")
        points = points + user_bet
    elif sum > 7 and user_number > 7:
        print("You won!")
        points = points + user_bet
    else:
        print("You are defeat.")
        points = points - user_bet

    print(f"you now have {points} points.")

    yes_no = input("Do you want to keep playing or no?(press enter to skip)")
    if yes_no == "no":
        break
    else:
        continue
