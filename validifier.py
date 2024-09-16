def is_valid_ship_placement(row, col, board, ship_size, orientation):
    """
    check if the given space is valid for ship placement.
    the space is valid if it is 0 (empty).
    
    row (int) - the row index where the ship is to be placed.
    col (int) - the column index where the ship is to be placed.
    board (list of lists) - the current game board holding ship placements.
    ship_size (int): the size of the ship being placed.
    orientation (str): the orientation of the ship.
    return - true if valid, false otherwise.
    """
    # check bounds based on orientation and ship size
    if orientation == 'horizontal':
        # check if ship fits within the board horizontally
        if col + ship_size > len(board[0]):
            return False
        # check if all the spaces in the row are empty (0)
        try:
            for i in range(ship_size):
                if board[row][col + i] != 0:
                    return False
        except:
            raise IndexError("Those coords are not permitted")

    elif orientation == 'vertical':
        # check if ship fits within the board vertically
        if row + ship_size > len(board):
            return False
        # check if all the spaces in the column are empty (0)
        try:
            for i in range(ship_size):
                if board[row + i][col] != 0:
                    return False
        except:
            raise IndexError("Those coords are not permitted")

    return True

def is_valid_shot(row, col):
    if row<=10 and col<=10:
        return True
    else:
        return False