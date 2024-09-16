# ooga booga main file
from game import Game

def main():
    game_on = True
    print("###  Welcome to Battleship!  ###")
    num = int(input("Enter number of ships (min = 1, max = 5): "))
    
    # Initializes Game and Player classes
    G = Game(num)
    P1 = G.get_P1()
    P2 = G.get_P2()
    
    # Establishes turn order
    order = [P1,P2]

    player = 1
    # For loop for placing ships for each player
    for p in order:
        print(f'Player {player} must place all {num} ships')
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
            player += 1

    
    print("YOU WIN!")

main()