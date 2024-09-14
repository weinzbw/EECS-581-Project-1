def is_valid_ship_placement(row, col, board):
    """
    check if the given space is valid for ship placement.
    the space is valid if it is 0 (empty).
    
    row (int) - the row index where the ship is to be placed.
    col (int) - the column index where the ship is to be placed.
    board (list of lists) - the current game board holding ship placements.
    return - true if valid, false otherwise.
    """
    # check bounds and if the space is empty (0)
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        # return true if the space is empty (0), otherwise false
        return board[row][col] == 0
    return False





def is_valid_shot(row, col, opp_board):
    """
    check if the given space is a valid shot.
    The space is valid if it is 1 aka a ship.
    
    row (int) - the row index where the shot is to be placed.
    col (int) - the column index where the shot is to be placed.
    opp_board (list of lists) - the current game board holding the opponent's ship placements.
    return - true if valid, false otherwise.
    """
    # Check bounds
    if 0 <= row < len(opp_board) and 0 <= col < len(opp_board[0]):
        # return true if shot is in bounds, else false
        return True
    return False