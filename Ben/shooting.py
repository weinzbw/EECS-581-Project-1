# Programs: Shooting, updateShots, isSunk, isAllSunk
# Description: this program allows the game class to let players fire shots
# at another player's board. This will also check if a ship has
# sunk and if all ships have sunk in order to end the game.
# Inputs: 2 integers representing the column and row of a shot.
# Outputs: A string that is either "miss" "hit" "sunk" or "all sunk"
# Author: Ben Weinzirl
# Creation Date: 9/12/24
# Current Time Spent: 1 hours 18 minutes

# Method called for the player that is shot at
def shot(player, x, y):
    # Checks if the square is valid, else it raises IndexError
    if is_valid_shot(x, y):
        # Saves the data of the square
        square = player.ships[x][y]
        # If the square is empty, it is a miss
        if square == 0:
            player.ships[x][y] = "M"
            return "miss"
        # If the sqaure has been hit before, raise IndexError
        elif square == 'X' or 'S' or "M":
            raise IndexError("Index picked before")
        # Otherwise, it is a hit
        else:
            # Checks if the ship is sunk
            if isSunk(player, square):
                # Checks if all ships are sunk
                if isAllSunk(player.ships):
                    player.ships[x][y] = "S"
                    return "all sunk"
                else:
                    player.ships[x][y] = "S"
                    return "sunk"
            else:
                player.ships[x][y] = "X"
                return "hit"
    else:
        raise IndexError("Index is not on the board")

# Updates the shot board of the player shooting
def updateShots(player, update, x, y):
    if update == "miss":
        player.shots[x][y] = "M"
    elif update == "hit":
        player.shots[x][y] = "X"
    else:
        player.shots[x][y] = "S"

# Checks if a ship is sunk
def isSunk(player, data):
    counter = 0
    # Iterates through every square on ship board
    for x in player.ships:
        for y in x:
            if y == data:
                counter += 1
    # If there is only one instance of the ship, it is now sunk
    if counter == 1:
        return True
    return False

# Checks if all ships are sunk
def isAllSunk(board):
    counter = 0
    # Iterates through every square on ship board
    for x in board:
        for y in x:
            if y == 1 or 2 or 3 or 4 or 5:
                counter += 1
    # If there is only one instance of any ship, then every ship is sunk
    if counter == 1:
        return True
    return False
