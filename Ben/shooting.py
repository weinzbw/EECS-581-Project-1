# Programs: Shooting
# Description: this program allows the player class to fire shots
# at another player's board. This will also check if a ship has
# sunk and if all ships have sunk in order to end the game.
# Inputs: 2 integers representing the column and row of a shot.
# Outputs: A string that is either "miss" "hit" "sunk" or "all sunk"
# Author: Ben Weinzirl
# Creation Date: 9/12/24
# Current Time Spent: 48 minutes

def shot(P1, P2, column, row):
    if isValid(column, row):
        square = P2.ships[column][row]
        if square == 0:
            P2.ships[column][row] = "M"
            return "miss"
        elif square == 'X' or 'S' or "M":
            raise IndexError("Index picked before")
        else:
            if isSunk(square):
                if isAllSunk(self.ships):
                    P2.ships[column][row] = "S"
                    return "all sunk"
                else:
                    P2.ships[column][row] = "S"
                    return "sunk"
            else:
                P2.ships[column][row] = "X"
                return "hit"
    else:
        raise IndexError("Index is not on the board")
    
def isSunk(player, data):
    counter = 0
    for column in player.ships:
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
