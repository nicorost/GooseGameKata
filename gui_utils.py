from itertools import cycle
from typing import List, Optional, Tuple

import pyxel

def draw_scene(
    player1: str, player2: str, 
    player1_space: Optional[int], player2_space: Optional[int],
    last_dice_roll: Optional[Tuple[int, int]],
    message: str,
    ):
    """Draws the board scene"""
    pyxel.cls(0)  # clear screen
    pyxel.text(5, 5, 'Game of the Goose', 2)
    draw_player_names(names=[player1, player2])
    draw_board()

    # Player Pieces
    if player1_space is not None:
        draw_piece(space=player1_space, color=9)
    if player2_space is not None:
        draw_piece(space=player2_space, color=10)
    
    if last_dice_roll is not None:
        roll1, roll2 = last_dice_roll
        draw_dice(roll1, roll2)
    
    draw_message(message, 5, 70)
    


def draw_piece(space: int, color: int = 9, xs: int = 15, ys: int = 40, width: int = 6):
    space = 64 - space  # reverse direction players move through the game.
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
    
    # start and end symbols
    pyxel.text(xs + width, ys + (2 * width), ">>>", 15)
    
    # Goose spaces
    pyxel.rect(xs + (6 * width), ys + (2 * width), width, width, 11)  # 4
    pyxel.rect(xs + (10 * width), ys + (2 * width), width, width, 11) # 8
    pyxel.rect(xs + (14 * width), ys + (1 * width), width, width, 11) # 13
    pyxel.rect(xs + (9 * width), ys + (1 * width), width, width, 11) # 18
    pyxel.rect(xs + (4 * width), ys + (1 * width), width, width, 11) # 23
    pyxel.rect(xs + (0 * width), ys + (1 * width), width, width, 11) # 27
    
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
    
    # bridge
    pyxel.rect(xs + (11 * width), ys + (1 * width) + 1, width, 2 * width - 2, 6)  
    pyxel.text(xs + (11 * width) + 1, ys + (2 * width) + 1, '^', 7)  
    pyxel.text(xs + (11 * width) + 1, ys + (2 * width) - 2, '^', 7)  
    
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
