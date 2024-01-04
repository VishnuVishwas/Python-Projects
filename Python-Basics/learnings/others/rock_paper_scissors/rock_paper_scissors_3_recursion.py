# Implementation of recursion

from enum import Enum
import sys
import random

def play_rock_paper_scissors():
    class RPS(Enum) :
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    user = int(input("\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"))

    if(user < 1 or user > 3):
        print("You must eneter 1, 2 or 3.")
        return play_rock_paper_scissors()

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
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain == "y":
            return play_rock_paper_scissors()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            break

play_rock_paper_scissors()

if __name__ == "__main__":
    play_rock_paper_scissors()