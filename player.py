# temp header
# class handling player data 
# time spent: 20m

import numpy as np # allows use of arrays

class Player:
    def __init__(self, num_ships):
        self.num_ships = num_ships
        
        # generate boards 
        self.ships, self.shots = np.zeros((10,10), dtype=int)
        
        '''code to place ships goes here?'''
    
    def return_board(self, num): # send board to game class
        if int(num) == 1: 
            return self.ships
        else:
            return self.shots 
        
    '''code to print boards goes here?'''
    
    