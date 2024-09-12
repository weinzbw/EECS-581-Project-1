# Programs: Shooting
# Description: this program allows the player class to fire shots
# at another player's board. This will also check if a ship has
# sunk and if all ships have sunk in order to end the game.
# Inputs: 2 integers representing the column and row of a shot.
# Outputs: A string that is either "miss" "hit" "sunk" or "all sunk"
# Author: Ben Weinzirl
# Creation Date: 9/12/24
# Current Time Spent: 38 minutes

def shot(column, row):
    if isValid(column, row):
        square = self.ships[column][row]
        if square == 0:
            self.ships[column][row] = "M"
            return "miss"
        elif square == 'X' or 'S' or "M":
            raise IndexError("Index picked before")
        else:
            if isSunk(square):
                if isAllSunk(self.ships):
                    self.ships[column][row] = "S"
                    return "all sunk"
                else:
                    self.ships[column][row] = "S"
                    return "sunk"
            else:
                self.ships[column][row] = "X"
                return "hit"
    else:
        raise IndexError("Index is not on the board")
    
def isSunk(data):
    counter = 0
    for column in self.ships:
        for row in column:
            if row == data:
                counter += 1
    if counter == 1:
        return True
    return False

def isAllSunk(board):
    counter = 0
    for column in board:
        for row in column:
            if row == 1 or 2 or 3 or 4 or 5:
                counter += 1

    if counter == 1:
        return True
    return False