# class handling player data 

import numpy as np # allows use of arrays

class Player:
    def __init__(self, num_ships):
        self.num_ships = num_ships
        
        # generate boards
        self.my_ships, self.opp_ships = np.zeros((10,10), dtype=int)
        
        '''call method to put ships on board'''
    
    def return_board(self, num):
        if int(num) == 1: 
            return self.my_ships 
        else:
            return self.opp_ships