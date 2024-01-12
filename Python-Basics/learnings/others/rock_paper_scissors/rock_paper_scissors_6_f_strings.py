import sys
import random
from enum import Enum


def rock_paper_scissors():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rock_paper_scissors():

        class RockPaperScissors(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(
            "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if player_choice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rock_paper_scissors()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

# used f strings
        print(f"\nYou chose  {str(RockPaperScissors(player)).replace('RockPaperScissors.', '').title()}.")
        print(f"Python chose {str(RockPaperScissors(computer)).replace('RockPaperScissors.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

# used f strings
        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins:  {str(player_wins)}")
        print(f"\nPython wins: { str(python_wins)}")

        print("\nPlay again?")

        while True:
            play_again = input("\nY for Yes or \nQ to Quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rock_paper_scissors()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return play_rock_paper_scissors


play = rock_paper_scissors()

play()