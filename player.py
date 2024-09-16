# temp header
# class handling player data 
# time spent: 20m

from typing import Literal, List

class Player:
    def __init__(self, num_ships: int):
        self.num_ships = num_ships
        
        # generate boards 
        self.ships = [[0 for _ in range(10)] for _ in range(10)]
        self.shots = [[0 for _ in range(10)] for _ in range(10)]
    
    def is_sunk(self, ship_size: int):
        x = self.ships.count(ship_size)
        if x == 0:
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
        
    