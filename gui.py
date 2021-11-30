from itertools import cycle
from typing import List

import pyxel

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


def draw_piece(space: int, color: int = 9, xs: int = 15, ys: int = 40, width: int = 6):
    if space <= 0:
        raise ValueError("space_num must be between 0 and 63")
    elif space <= 16:
        pyxel.circ(xs + ((space - 1) * width) + 3, ys + 3, width // 2 - 2, color)
    elif space <= 19:
        pyxel.circ(xs + ((16 - 1) * width) + 3, ys + ((space - 16) * width) + 3, width // 2 - 2, color)
    elif space <= 34:
        x = xs + (16 - (space - 18)) * width + 3
        pyxel.circ(x, ys + (3 * width) + 3, width // 2 - 2, color)
    elif space <= 36:
        y = ys + (4 - (space - 33)) * width + 3
        pyxel.circ(xs + 3, y, width // 2 - 2, color)
    elif space <= 50:
        pyxel.circ(xs + ((space - 36) * width) + 3, ys + (1 * width) + 3, width // 2 - 2, color)
    elif space <= 51:
        pyxel.circ(xs + ((15 - 1) * width) + 3, ys + ((space - 50 + 1) * width) + 3, width // 2 - 2, color)
    elif space <= 63:
        x = xs + (16 - (space - 49)) * width + 3
        pyxel.circ(x, ys + (2 * width) + 3, width // 2 - 2, color)
    else:
        raise ValueError("space_num must be between 0 and 63")
        

def draw_board(xs: int = 15, ys: int = 40, width=6):
    # make checkerboard pattern
    colors = cycle([5, 7])
    pyxel.rect(xs - width, ys, width, width, 7)
    for x in range(xs, xs + width * 16, width):
        next(colors)
        for y in range(ys, ys + width * 4, width):
            color = next(colors)
            pyxel.rect(x, y, width, width, color)
    pyxel.rect(xs + width, ys + (2 * width), width, width, color)  # duplicate color for unused square 64
    
    #  Make line that shows track
    line_color = lc = 0
    pyxel.line(xs - 1, ys - 1, xs + (16 * width), ys - 1, lc)
    pyxel.line(xs - 1, ys + (4 * width), xs + (16 * width), ys + (4 * width), lc)
    pyxel.line(xs - 1, ys + width, xs - 1, ys + (3 * width) - 1, lc)
    pyxel.line(xs + (16 * width), ys - 1, xs + (16 * width), ys + (4 * width) - 1, lc)
    pyxel.line(xs, ys + width, xs + (15 * width) - 1, ys + width , lc)
    pyxel.line(xs + (15 * width) - 1, ys + width, xs + (15 * width) - 1, ys + (3 * width) - 1 , lc)
    pyxel.line(xs + (1 * width),  ys + (3 * width) - 1, xs + (15 * width) - 1, ys + (3 * width) - 1 , lc)
    pyxel.line(xs + (1 * width),  ys + (2 * width) - 0, xs + (1 * width), ys + (3 * width) - 1 , lc)
    pyxel.line(xs + (1 * width),  ys + (2 * width) - 0, xs + (14 * width) - 1,  ys + (2 * width) - 0 , lc)
    
    
def draw_player_names(names: List[str], xs: int = 5, ys: int = 15):
    pyxel.text(xs, ys, f'Players: {"  ".join(names)}', 2)
    

def draw_die(side: int, xs: int, ys: int):
    pyxel.rect(xs, ys, 7, 7, col=7)
    pips = {
        1: [(3, 3)],
        2: [(1, 1), (5, 5)],
        3: [(1, 1), (3, 3), (5, 5)],
        4: [(1, 1), (1, 5), (5, 1), (5, 5)],
        5: [(1, 1), (1, 5), (3, 3), (5, 1), (5, 5)],
        6: [(1, 1), (1, 3), (1, 5), (5, 1), (5, 3), (5, 5)],
    }
    for x, y in pips[side]:
        pyxel.rect(xs + x, ys + y, 1, 1, 0)
        
        
def draw_dice(side1, side2, xs: int = 5, ys: int = 23, text_col: int = 2):
    pyxel.text(xs, ys + 2, "Roll: ", col=text_col)
    draw_die(side=side1, xs=xs + 25, ys=ys)
    draw_die(side=side2, xs=xs + 35, ys=ys)
    
    
def draw_message(message: str, xs: int, ys: int, col: int = 2):
    pyxel.text(xs, ys, message, col)
