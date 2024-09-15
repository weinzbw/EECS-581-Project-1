# ooga booga main file
from game import Game

def main():
    game_on = True
    print("###  Welcome to Battleship!  ###")
    num = input("Enter number of ships (min = 1, max = 5): ")
    print("### Game Start! ###")
    
    G = Game(num)
    P1 = G.get_P1()
    P2 = G.get_P2()
    
    order = [P1,P2]
    
    while game_on is not P1.is_all_ships_sunk and not P2.is_all_ships_sunk:
        player = 1
        for p in order:
            print(f'Player {player}s turn')
            p.print_board(p.shots)
            G.turn(p, order[order.index(p)-1])
            player += 1
    
    print("YOU WIN!")

main()