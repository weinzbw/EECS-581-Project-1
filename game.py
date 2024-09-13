# temp header
# class handling game data and actions
# time spent: m

from player import Player

class Game:
    def __init__(self):
        num = input("Enter number of starting ships: ") # add err handling later
        P1, P2 = Player(num)
        
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
        