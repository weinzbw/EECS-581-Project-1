# Program: main
# Description: This program implements the Game and Player classes from their respective files.
# This creates a 2-player battleship, letting players input coordinates to both place and sink ships.
# Inputs: # of ships, coordinates
# Outputs: game states via a 2D Array
# Author: Del Endecott, Ben Weinzirl
# Creation Date: 9/15/24

from game import Game

def main():
    game_on = True
    print("###  Welcome to Battleship!  ###")
    try:
        num = int(input("Enter number of ships (min = 1, max = 5): "))
    except:
        print("num must be an integer")
        return 0
    
    if num < 1 or num > 5:
        print("You can only have 1 through 5 ships")
        main()
        return 0
    
    # Initializes Game and Player classes
    G = Game(num)
    P1 = G.get_P1()
    P2 = G.get_P2()
    
    # Establishes turn order
    order = [P1,P2]

    player = 1
    # For loop for placing ships for each player
    for p in order:
        print(f'Player {player} must place all {num} ships, starting from smallest')
        player += 1
        for i in range(num):
            G.place_ship(p, i+1)

    print("### Game Start! ###")
    # While loop for running the game until all of an opponents ships are sunk
    while game_on:
        player = 1
        for p in order:
            print(f'Player {player}s turn')
            p.print_board(0)
            G.turn(p, order[order.index(p)-1])
            if order[order.index(p)-1].is_all_sunk():
                game_on = False
                p.print_board(0)
                break
            player += 1

    
    print("YOU WIN!")

main()
