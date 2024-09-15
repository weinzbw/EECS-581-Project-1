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
    
    while game_on:
        for p in order:
            pass