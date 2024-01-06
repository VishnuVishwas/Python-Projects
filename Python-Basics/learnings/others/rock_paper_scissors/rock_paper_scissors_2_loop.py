# implementation of loop 

from enum import Enum
import sys
import random

class RPS(Enum) :
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

while True:
    user = int(input("\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"))
    if(user < 1 or user > 3):
        sys.exit("You must eneter 1, 2 or 3.")

    system = int(random.choice("123"))

    print("You chose : " + str(RPS(user)).replace('RPS.', "").title())
    print("Computer chose : " + str(RPS(system).name))

    if user == 1 and system == 3:
        print("🎉 You win!")
    elif user == 2 and system == 1:
        print("🎉 You win!")
    elif user == 3 and system == 2:
        print("🎉 You win!")
    elif user == system:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")
    
    while True:
        playagain = print("Wanna play again? Y or Q")
        if playagain.lower() == 'y':
            continue
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            playagain = False

sys.exit("Bye! 👋")

