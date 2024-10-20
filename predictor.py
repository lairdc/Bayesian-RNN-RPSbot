import time
from linkedList import *
import sys
import random

class Predictor:
    def __init__(self):
        # Initialize any state if needed (for now we don't need anything)
        self.move_history = LinkedList()
        pass
    
    def predict_next_move(self):
        """
        Always predict 'Rock' as the next move.
        
        :param player_moves: A list of the player's previous moves
        :return: 'Rock'
        """
        #time.sleep(1)
        print("predicting...")
        sys.stdout.flush()
        prediction = random.randint(0,2)
        return self.convert_predicition(prediction)

    def convert_predicition(self, prediction):
        if prediction == 0: #Thinks player will play rock
            return 1
        elif prediction == 1:
            return 2
        else:
            return 0

    def add_move(self, move):
        if move != None:
            self.move_history.add_to_front(move)
        print("added_move:", move)
        print("full history:", self.move_history)
