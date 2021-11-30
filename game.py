

from typing import Optional, Tuple


class Game:
    
    def __init__(self, player1: str, player2: str) -> None:
        pass
    
    def get_player1_name(self) -> str:
        return ""
    
    def get_player2_name(self) -> str:
        return ""
    
    def get_player1_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 1 is currently on"""
        return None
    
    def get_player2_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 2 is currently on"""
        return None
    
    def last_dice_roll(self) -> Optional[Tuple[int, int]]:
        """Returns either None or a pair of die rolls, like (2, 6)"""
        return None
        
    def get_current_player(self) -> str:
        return ''
    
    def roll_dice(self) -> None:
        """Updates the game in-place by rolling dice."""
        ...
        
    def is_over(self) -> bool:
        """Returns True if game is over."""
        return False
    
    def get_winner(self) -> Optional[str]:
        """Returns None or the name of the winner"""
        return None
    
    
    