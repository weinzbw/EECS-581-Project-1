# Program: player
# Description: This program is utilized by the game file in order to run Battleship.
# It focused on creating a lot of needed values for the game file, like the boards of ships and shots.
# It also checks the state of the game, with is_sunk, and is_all_sunk, as well as printing the board.
# Inputs: num_ships, ship_size, num 
# Outputs: board of ships, board of shots, Booleans determining status of sunk states, printed board, returned board
# Author: Del Endecott, Mick Torres
# Creation Date: 9/11/24

from typing import Literal, List

class Player:
    def __init__(self, num_ships: int):
        self.num_ships = num_ships
        
        # generate boards 
        self.ships = [[0 for _ in range(10)] for _ in range(10)]
        self.shots = [[0 for _ in range(10)] for _ in range(10)]
    
    def is_sunk(self, ship_size: int):
        x = 0
        for line in self.ships:
            x += line.count(ship_size)
        if x == 1:
            return True
        else:
            return False
        
    def is_all_sunk(self):
        if self.num_ships > 0:
            return False
        else:
            return True
    
    def return_board(self, num): # send board to game class
        if int(num) == 1: 
            return self.ships
        else:
            return self.shots 
        
    def print_board(self, num):
        coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        i = 0
        if int(num) == 1:
            print('    1  2  3  4  5  6  7  8  9  10\n')
            for row in self.ships:
                print(coords[i], ' ', '  '.join(map(str, row)), '\n')
                i += 1
        else:
            print('    1  2  3  4  5  6  7  8  9  10\n')
            for row in self.shots:
                print(coords[i], ' ', '  '.join(map(str, row)), '\n')
                i += 1
        print('\n----------------------------------\n')
        
    