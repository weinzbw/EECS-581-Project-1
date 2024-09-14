# temp header
# class handling game data and actions
# time spent: m

from player import Player
import validifier as v

class Game:
    def __init__(self, num: int):
        self.P1, self.P2 = Player(num)
        
    def get_P1(self):
        return self.P1
    
    def get_P2(self):
        return self.P2
        
    def shot(player, x, y): # player = player being shot AT
    # Checks if the square is valid, else it raises IndexError
        if v.is_valid_shot(x, y):
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
                if player.is_sunk(square):
                    # Checks if all ships are sunk
                    if player.is_all_sunk():
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
        