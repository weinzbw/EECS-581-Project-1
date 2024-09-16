# Program: game
# Description: This program utilizes the Player class, and the functions from validifier.
# It brings everything together in order to run a game of Battleship.
# The Game class manages player turns, ship placement, and shot processing.
# It handles input validation through validifier.
# Inputs: num, player, ship_size, row, col, ships, orientation, target, y, x, letter
# Outputs: player, num, game states via 2D Array, messages pertaining to the changes in game states
# Author: Del Endecott, Sam Harrison, Mick Torres
# Creation Date: 9/11/24
from typing import Literal, List

from player import Player
import validifier as v

class Game:
    def __init__(self, num: int):
        self.P1 = Player(num)
        self.P2 = Player(num)
        
    def get_P1(self):
        return self.P1
    
    def get_P2(self):
        return self.P2
    
    def place_ship(self, player, ship_size: int):
        def letter_to_index(letter: str) -> int:
            return ord(letter.upper()) - ord('A')
    
        position = input("Input the ship's top-leftmost position (e.g., A6): ").strip()
        orientation = input("Input the orientation of the ship (horizontal or vertical): ").strip().lower()
        
        try:
            row = letter_to_index(position[0])  # converts characters to numbers
            col = int(position[1:]) - 1         # subtracts 1 due to 0-indexed
        except:
            print("Invalid coordinate format. Please try again")
            self.place_ship(player, ship_size)
        try:
            if v.is_valid_ship_placement(row, col, player.ships, ship_size, orientation):
                # the temp_board has the ships' sizes as identifiers of where they are placed
                if orientation == 'horizontal':
                # places ship horizontally by changing line of cells
                # increases column index for length of ship
                    for i in range(ship_size):
                        player.ships[row][col + i] = ship_size 
        
                elif orientation == 'vertical':
                    # places ship vertically by changing line of cells
                    # increases row index for length of ship
                    for i in range(ship_size):
                        player.ships[row + i][col] = ship_size
            
                else:
                    print("Please check spelling of horizontal or vertical and try again")
                    self.place_ship(player, ship_size)
            else:
                print("Invalid ship placement, try again")
                self.place_ship(player, ship_size)
        except:
            print("That format is invalid, please try again")
            self.place_ship(player, ship_size)

        
    def shot(self, player, target, y, x): # player = player being shot AT (x and y are swapped due to 2D array)
    # Checks if the square is valid, else it raises IndexError
        if v.is_valid_shot(x, y):
            # Saves the data of the square
            square = target.ships[x][y]
            # If the square is empty, it is a miss
            if square == 0:
                player.shots[x][y] = "M"
                return "missed!"
            # If the square has been hit before, raise IndexError
            elif player.shots[x][y] == 'X' or player.shots[x][y] == 'M' or player.shots[x][y] == "S":
                raise IndexError("Index picked before")
            # Otherwise, it is a hit
            else:
                # Checks if the ship is sunk
                if target.is_sunk(square):
                    target.num_ships -= 1
                    # Checks if all ships are sunk
                    if target.is_all_sunk():
                        player.shots[x][y] = "S"
                        return "Sunk all your opponent's ships!"
                    else:
                        player.shots[x][y] = "S"
                        return "You sunk a ship!"
                else:
                    player.shots[x][y] = "X"
                    target.ships[x][y] = "X"
                    return "You hit a ship!"
        else:
            raise IndexError("Index is not on the board")
    
    def turn(self,player,target):
        try:
            position = input("Input the square you want to shoot (e.g., A6): ")
            y = ord(position[0].upper()) - ord('A')  # converts characters to numbers
            x = int(position[1:]) - 1         # subtracts 1 due to 0-indexed
        except:
            print("Please pay attention to coordinate input formatting")
            self.turn(player, target)
        #shot() method can raise an error with invalid input
        try:
            shot = self.shot(player, target, x, y)
            print(shot)
            # Takes another turn if it is a hit
            if shot == "You hit a ship!" or shot == "You sunk a ship!":
                player.print_board(0)
                self.turn(player, target)
        # Gives another chance to input proper coords if an error is raised
        except:
             print("Invalid shot, try again")
             self.turn(player, target)
