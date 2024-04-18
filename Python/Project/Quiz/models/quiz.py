# quiz.py
from .player import Player
from .question import Question
import csv
import random

class Quiz:
    def __init__(self, player):
        self.player = player
        self.mcq_questions = []
        self.true_false_questions = []
        self.short_questions = []

    # load questions from csv file
    def load_questions_from_csv(self, file_name):
        try:
            with open(f'data/{file_name}', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if file_name == 'mcq_questions.csv':
                        question_type = 1
                        question_text, option_A, option_B, option_C, option_D, answer_text = map(str.strip, row)
                        
                        question_instance = Question(question_type, question_text, option_A, option_B, option_C, option_D, answer_text)
                        self.mcq_questions.append(question_instance)

                    elif file_name == 'true_false_questions.csv':
                        question_type = 2
                        question_text, answer_text = map(str.strip, row)
                        
                        question_instance = Question(question_type, question_text, answer_text=answer_text)
                        self.true_false_questions.append(question_instance)

                    elif file_name == 'short_questions.csv':
                        question_type = 3
                        question_text, answer_text = map(str.strip, row)
                        
                        question_instance = Question(question_type, question_text, answer_text=answer_text)
                        self.short_questions.append(question_instance)
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except Exception as e:
            print(f"Error loading {file_name}:", str(e))

    # play quiz
    def play_quiz(self, question_type):
        # create question instance
        if question_type == 1:
            print("\nPlayer choice:", Question.QuestionType(question_type).name)
            print("Questions: ")

            self.load_questions_from_csv('mcq_questions.csv')
            
            for question in self.mcq_questions:
                print(f"\n{question.question_text}")
                print(f"Options\nA. {question.option_A}\nB. {question.option_B}\nC. {question.option_C}\nD. {question.option_D}")

                user_answer = input("Your Choice: ")
                question.check_mcq_answer(user_answer, self.player)
            
        elif question_type == 2:
            print("\nPlayer choice:", Question.QuestionType(question_type).name)
            print("Questions: ")

            self.load_questions_from_csv('true_false_questions.csv')
            
            for question in self.true_false_questions:
                print(f"\n{question.question_text}")
                print(f"Options\nA. True\nB. False")
                user_answer = input("Your choice: ")
                
                question.check_true_false_answer(user_answer, self.player)

        elif question_type == 3:
            print("\nPlayer choice:", Question.QuestionType(question_type).name)
            print("Questions: ")

            self.load_questions_from_csv('short_questions.csv')

            for question in self.short_questions:
                print(f"\n{question.question_text}")
                user_answer = input("Answer in one word: ")
                
                question.check_short_answer(user_answer, self.player)

if __name__ == '__main__':
    player = Player('vishnu')
    quiz_instance = Quiz(player)

    quiz_instance.load_questions_from_csv('mcq_questions.csv')
    quiz_instance.play_quiz(1)

    quiz_instance.load_questions_from_csv('true_false_questions.csv')
    quiz_instance.play_quiz(2)

    quiz_instance.load_questions_from_csv('short_questions.csv')
    quiz_instance.play_quiz(3)
