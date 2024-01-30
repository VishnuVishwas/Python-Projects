# player.py
class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0

    # update player score 
    def update_score(self):
        self.player_score += 1

    # view player score
    def view_score(self):
        print(f"Current score of {self.player_name} is: {self.player_score}") 

