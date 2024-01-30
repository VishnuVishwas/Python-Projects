from models.quiz import Quiz
from models.player import Player

def create_player(player_list):
    player_name = input("Enter the player name: ")
    player = Player(player_name)
    player_list.append(player)
    print(f"Player {player_name} created successfully.")
    return player  

def view_scores(player_list):
    if not player_list:
        print("No players found. Create a player first.")
        return

    print("\nPlayer Scores:")
    for player in player_list:
        player.view_score()

def play_quiz(player_list, quiz_instance):
    if not player_list:
        print("No players found. Create a player first.")
        return

    print("\nSelect player to start quiz")
    for i, player in enumerate(player_list):
        print(f"{i + 1}. {player.player_name}")

    try:
        player_index = int(input("Enter the player index: ")) - 1

        if 0 <= player_index < len(player_list):
            selected_player = player_list[player_index]

            while True:
                print("\nChoose from one of the 3 quizzes: ")
                print("1. MCQ\n2. True or False\n3. Short answer questions")
                print("4. Back to Main Menu")

                question_choice = input("Enter the index of question type: ")

                if question_choice == '1':
                    quiz_instance.player = selected_player  # Set the player instance in the quiz
                    quiz_instance.play_quiz(1)  # MCQ
                elif question_choice == '2':
                    quiz_instance.player = selected_player
                    quiz_instance.play_quiz(2)  # True/False
                elif question_choice == '3':
                    quiz_instance.player = selected_player
                    quiz_instance.play_quiz(3)  # Short Answer
                elif question_choice == '4':
                    break  # Back to Main Menu
                else:
                    print("Invalid option. Please try again.")

        else:
            print("Invalid player number. Please try again.")
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))
    finally:
        input("Press Enter to continue...")

def main():
    player_list = []
    quiz_instance = Quiz(None)  

    while True:
        print("\nOptions")
        print("1. Create player")
        print("2. Play quiz")
        print("3. View Scores")
        print("4. Quit")

        try:
            player_choice = input("Enter your choice: ")

            if player_choice == '1':
                create_player(player_list)
            elif player_choice == '2':
                play_quiz(player_list, quiz_instance)
            elif player_choice == '3':
                view_scores(player_list)
            elif player_choice == '4':
                print("Thank you for playing 😊")
                break
            else:
                print("Choose a valid option.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))

if __name__ == '__main__':
    main()
