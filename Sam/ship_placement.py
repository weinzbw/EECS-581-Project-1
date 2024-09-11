#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Programs: place_ship and letter_to_index
# Description: this program places down ships on the array by starting at the top-leftmost position 
# and going either down or right depending on the horizontal or vertical direction
# the temp_board may have to be replaced in future iterations depending on how well it
# functions with the team's code
# Inputs: player_num, ship_size, orientation; letter
# Outputs: temp_board
# Author: Samuel Harrison
# Creation Date: 9/11/24
# Current Time Spent: 52 minutes

from typing import Literal, List

def place_ship(player_num: int, ship_size: int, orientation: Literal['horizontal', 'vertical']) -> List:
    def letter_to_index(letter: str) -> int:
        return ord(letter.upper()) - ord('A')
    
    temp_board = [[0 for _ in range(10)] for _ in range(10)] #initializes blank 10x10 board (replace/remove later)
    
    position = input("Input the ship's top-leftmost position (e.g., A6): ").strip()
    
    row = letter_to_index(position[0])  # converts characters to numbers
    col = int(position[1:]) - 1         # subtracts 1 due to 0-indexed
    
    # the temp_board has the ships' sizes as identifiers of where they are placed
    if orientation == 'horizontal':
    # places ship horizontally by changing line of cells
    # increases column index for length of ship
        for i in range(ship_size):
            temp_board[row][col + i] = ship_size 
        
    elif orientation == 'vertical':
        # places ship vertically by changing line of cells
        # increases row index for length of ship
        for i in range(ship_size):
            temp_board[row + i][col] = ship_size
            
    return temp_board

# example usage (remove later)
# player_num, ship_size, orientation
board = place_ship(2, 1, 'vertical')
for row in board:
    print(row)

