# Rock, paper & scissors game

from enum import Enum 
import sys
import random

class RockPaperScissors(Enum) :
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

player_choice = int(input("Enter your choice : \n1.Rock\n2. Paper\n3. Scissors : \n"))

if(player_choice < 1 | player_choice > 3):
    sys.exit("Your choice should be either 1, 2 or 3")

computer_choice = int(random.choice("123"))

print("Your choice : ", str(RockPaperScissors(player_choice).name))
print("Computer choice : " + str(RockPaperScissors(computer_choice).name)) 

if player_choice == 1 and computer_choice == 3 :
    print("🏆 You won")
elif player_choice == 2 and computer_choice == 1:
    print("🏆 You won")
elif player_choice == 3 and computer_choice == 2:
    print("🏆 You won")
elif player_choice == computer_choice:
    print("🤝 Tie")
else:
    print("💻 computer wins")

