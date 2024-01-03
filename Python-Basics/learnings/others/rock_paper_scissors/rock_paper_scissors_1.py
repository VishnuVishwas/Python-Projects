# Rock, paper & scissors game

from enum import Enum 
import sys
import random

class RockPaperScissors(Enum) :
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playerChoice = int(input("Enter your choice : \n1.Rock\n2. Paper\n3. Scissors : \n"))

if(playerChoice < 1 | playerChoice > 3):
    sys.exit("Your choice should be either 1, 2 or 3")

computerChoice = int(random.choice("123"))

print("Your choice : " + str(RockPaperScissors(playerChoice).name))
print("Computer choice : " + str(RockPaperScissors(computerChoice).name)) 

if playerChoice == 1 and computerChoice == 3 :
    print("🏆 You won")
elif playerChoice == 2 and computerChoice == 1:
    print("🏆 You won")
elif playerChoice == 3 and computerChoice == 2:
    print("🏆 You won")
elif playerChoice == computerChoice:
    print("🤝 Tie")
else:
    print("💻 computer wins")

