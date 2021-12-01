from gui import Gui
from game import Game
   

game = Game(player1='Julia', player2='Joe')
gui = Gui(game=game)
gui.run()
