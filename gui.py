import pyxel

from gui_utils import draw_dice, draw_piece, draw_board, draw_message, draw_player_names
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
                print(f'Rolling Dice for player {self.game.get_current_player()}')
                self.game.roll_dice()
            else:
                print('Game is over. Exit game to Restart.')
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
    def draw(self):
        """Draws the graphics."""
        pyxel.cls(0)  # clear screen
        pyxel.text(5, 5, 'Game of the Goose', 2)
        draw_player_names(names=[
            self.game.get_player1_name(), 
            self.game.get_player2_name(),
        ])
        draw_board()
        space = self.game.get_player1_space()
        if space is not None:
            draw_piece(space=space, color=9)
            
        space = self.game.get_player2_space()
        if space is not None:
            draw_piece(space=space, color=10)
        
        dice_rolls = self.game.last_dice_roll()
        if dice_rolls is not None:
            roll1, roll2 = dice_rolls
            draw_dice(roll1, roll2)
        
        if not self.game.is_over():
            draw_message(self.message, 5, 70)
        else:
            draw_message(f"{self.game.get_winner()} won!")
        
    def run(self):
        pyxel.run(self.update, self.draw)

