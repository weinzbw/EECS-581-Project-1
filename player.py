# temp header
# class handling player data 
# time spent: 20m

import numpy as np # allows use of arrays
from typing import Literal, List

class Player:
    def __init__(self, num_ships: int):
        self.num_ships = num_ships
        
        # generate boards 
        self.ships, self.shots = np.zeros((10,10), dtype=int)
        
        '''ship-placing code written by Sam'''
    
    def place_ship(self, ship_size: int, orientation: Literal['horizontal', 'vertical']) -> List:
        def letter_to_index(letter: str) -> int:
            return ord(letter.upper()) - ord('A')
            
        position = input("Input the ship's top-leftmost position (e.g., A6): ").strip()
        
        row = letter_to_index(position[0])  # converts characters to numbers
        col = int(position[1:]) - 1         # subtracts 1 due to 0-indexed
            
        # the board has the ships' sizes as identifiers of where they are placed
        if orientation == 'horizontal':
        # places ship horizontally by changing line of cells
        # increases column index for length of ship
            for i in range(ship_size):
                self.ships[row][col + i] = ship_size 
                
        elif orientation == 'vertical':
            # places ship vertically by changing line of cells
            # increases row index for length of ship
            for i in range(ship_size):
                self.ships[row + i][col] = ship_size
                    
        return self.ships
    
    def is_sunk(self, ship_size: int):
        x = self.ships.count(ship_size)
        if x == 0:
            self.num_ships -= 1
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
        
    def print_boards(self, num): # add self
        coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        i = 0
        if int(num) == 1:
            print('    1  2  3  4  5  6  7  8  9  10\n')
            for row in self.ships:  # change to self.ships
                print(coords[i], ' ', '  '.join(map(str, row)), '\n')
                i += 1
        else:
            print('    1  2  3  4  5  6  7  8  9  10\n')
            for row in self.shots: # change to self.shots
                print(coords[i], ' ', '  '.join(map(str, row)), '\n')
                i += 1
        print('\n----------------------------------\n')
        
    