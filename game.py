

from typing import Optional, Tuple


class Game:
    
    def __init__(self, player1: str, player2: str) -> None:
        self.player1 = player1  # Save player1 data in self.player1
    
    def get_player1_name(self) -> str:
        "Returns the name of Player 1 as a string."
        return ""
    
    def get_player2_name(self) -> str:
        "Returns the name of Player 2 as a string."
        return ""
    
    def get_player1_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 1 is currently on"""
        return 8
    
    def get_player2_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 2 is currently on"""
        return 2
        
    def get_current_player(self) -> str:
        """Returns the name of the current player."""
        return ''
    
    def roll_dice(self) -> None:
        """Updates the game in-place by rolling dice."""
        ...
        
    def get_last_dice_roll(self) -> Optional[Tuple[int, int]]:
        """Returns either None or a pair of die rolls, like (2, 6)"""
        return None
        
    def is_over(self) -> bool:
        """Returns True if game is over."""
        return False
    
    def get_winner(self) -> Optional[str]:
        """Returns None (if the game is not over) or the name of the winner"""
        return None
    
    
    