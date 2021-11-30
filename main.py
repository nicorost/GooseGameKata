from gui import Gui
from game import Game
   
player1_name = 'Julia'   
player2_name = 'Joe'
# player1_name = input("Player 1 Name: ")
# print(f"Player 1: {player1_name}")
# player2_name = input("Player 2 Name: ")
# print(f"Player 2: {player2_name}")

game = Game(player1=player1_name, player2=player2_name)
gui = Gui(game=game)
gui.run()
