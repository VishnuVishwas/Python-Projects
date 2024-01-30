# question.py
from enum import Enum
from .player import Player

class Question:
    QuestionType = Enum('QuestionType', {'MCQ_QUESTIONS': 1, 'TRUE_FALSE': 2, 'SHORT_ANSWERS': 3})
    
    def __init__(self, question_type, question_text, option_A=None, option_B=None, option_C=None, option_D=None, answer_text=None, player=None):
        if question_type not in [1, 2, 3]:
            print("Invalid choice.")
            exit()

        if question_type == 1:
            self.create_mcq_question(question_text, option_A, option_B, option_C, option_D, answer_text)
        elif question_type == 2:
            self.create_true_false_question(question_text, answer_text)
        elif question_type == 3:
            self.create_short_answer_question(question_text, answer_text)

    # create mcq question instance
    def create_mcq_question(self, question_text, option_A, option_B, option_C, option_D, mcq_answer):
        self.question_text = question_text
        self.option_A = option_A
        self.option_B = option_B
        self.option_C = option_C
        self.option_D = option_D
        self.mcq_answer = mcq_answer
        self.player = None

    # create true/false question instance
    def create_true_false_question(self, question_text, true_false_answer):
        self.question_text = question_text
        self.true_false_answer = true_false_answer
        self.player = None

    # create short question instance
    def create_short_answer_question(self, question_text, short_answer):
        self.question_text = question_text
        self.short_answer = short_answer
        self.player = None

    # check mcq answer
    def check_mcq_answer(self, user_mcq_answer, player):
        if not user_mcq_answer.strip():
            print("Invalid input. Please provide an answer.")
            return
    
        if self.mcq_answer.strip().lower() == user_mcq_answer.strip().lower():
            print("You are right 👏")
            player.update_score()
            player.view_score()
        else:
            print(f"Oops!!\nThe correct answer is: {self.mcq_answer}")
            player.view_score()

    # check true/false answer
    def check_true_false_answer(self, user_flag_answer, player):
        if not user_flag_answer.strip():
            print("Invalid input. Please provide an answer.")
            return

        if self.true_false_answer.strip().lower() == user_flag_answer.strip().lower():
            print("You are right 👏")
            player.update_score()
            player.view_score()
        else:
            print(f"Oops!!\nThe correct answer is: {self.true_false_answer}")
            player.view_score()

    # check short question answer
    def check_short_answer(self, user_short_answer, player):
        if not user_short_answer.strip():
            print("Invalid input. Please provide an answer.")
            return

        if self.short_answer.strip().lower() == user_short_answer.strip().lower():
            print("You are correct")
            player.update_score()
            player.view_score()
        else:
            print("Incorrect. Actual answer is:", self.short_answer)
            player.view_score()


