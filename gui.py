import pyxel

from gui_utils import draw_scene
from game import Game


class Gui:
    
    def __init__(self, game: Game, title="Game of the Goose") -> None:
        self.game = game
        self.title = title
        self.message = "Press Space to Roll Dice"
        self._start_gui()
        
    def _start_gui(self):
        """Creates a graphics window."""
        pyxel.init(120, 80, caption=self.title)
        
    def update(self):
        """Runs every frame.  It's meant to take and direct user input."""
        if pyxel.btnp(pyxel.KEY_SPACE):
            if not self.game.is_over():
                print(f'Rolling Dice for player: {self.game.get_current_player()}')
                self.game.roll_dice()
            else:
                print('Game is over. Exit game to Restart.')
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
    def draw(self):
        """Draws the graphics."""
        draw_scene(
            player1=self.game.get_player1_name(),
            player2=self.game.get_player2_name(),
            player1_space=self.game.get_player1_space(),
            player2_space=self.game.get_player2_space(),
            last_dice_roll=self.game.get_last_dice_roll(),
            message=self.message if not self.game.is_over() else f"{self.game.get_winner()} won!",
        )
       
        
    def run(self):
        pyxel.run(self.update, self.draw)

