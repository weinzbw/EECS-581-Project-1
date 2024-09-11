board = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
];

def print_boards(board):
    for row in board:
        print(' '.join(map(str, row)))

print_boards(board)