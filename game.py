import random
import sys
from predictor import Predictor

class Game:
    def __init__(self):
        self.player_move = None
        self.bot_move = None
        self.round_result = None
        self.player_moves = []  # Track the player's move history
        self.win_count = 0
        self.tie_count = 0
        self.loss_count = 0
        self.predictor = Predictor()

    def bot_predict_move(self):
        """Bot predicts the player's next move based on history."""
        print("predicting...", self.player_move)
        self.predictor.add_move(self.player_move)
        sys.stdout.flush()

        self.bot_move = self.predictor.predict_next_move()  # Randomly pick Rock (0), Paper (1), or Scissors (2)

    def play_round(self, player_move):
        """Process a round of RPS and determine the result."""
        self.player_move = player_move
        self.player_moves.append(player_move)
        print(f"player: {self.player_move}, bot move: {self.bot_move}")
        sys.stdout.flush()

        # Determine round result (rock beats scissors, etc.)
        if self.player_move == self.bot_move:
            self.round_result = "Tie"
            self.tie_count += 1
        elif (self.player_move == 0 and self.bot_move == 2) or \
             (self.player_move == 1 and self.bot_move == 0) or \
             (self.player_move == 2 and self.bot_move == 1):
            self.round_result = "Player Wins!"
            self.win_count += 1
        else:
            self.round_result = "Bot Wins!"
            self.loss_count += 1

    def reset_round(self):
        """Reset the game state for the next round and immediately predict bot's next move."""
        self.player_move = None
        self.round_result = None
        #self.bot_predict_move()  # Bot predicts the next move immediately
