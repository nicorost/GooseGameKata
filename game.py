
import random
from typing import Optional, Tuple


class Game:
    
    def __init__(self, player1: str, player2: str) -> None:
        self.player1 = player1  # Save player1 data in self.player1
        self.player2 = player2  # Save player2 data in self.player2
        self.player1_space = None
        self.player2_space = None
        self.current_player = self.player1
        self.d1 = None
        self.d2 = None
    
    def get_player1_name(self) -> str:
        """Returns the name of Player 1 as a string."""
        return self.player1
    
    def get_player2_name(self) -> str:
        """Returns the name of Player 2 as a string."""
        return self.player2
    
    def get_player1_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 1 is currently on"""
        return self.player1_space
    
    def get_player2_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 2 is currently on"""
        return self.player2_space
        
    def get_current_player(self) -> str:
        """Returns the name of the current player."""
        return self.current_player
    
    def roll_dice(self) -> None:
        """Updates the game in-place by rolling dice."""
        self.d1 = random.randint(1, 6)
        self.d2 = random.randint(1, 6)
        number = self.d1 + self.d2
        if self.current_player == self.player1:
            if self.player1_space is None:
                self.player1_space = 0
            if self.player1_space + number < 64:
                self.player1_space = self.player1_space + number
            if self.player1_space == 9:
                self.player1_space = 16
            if self.player1_space not in [4, 8, 13, 18, 23, 27]:
                self.current_player = self.player2
        else:
            if self.player2_space is None:
                self.player2_space = 0
            if self.player2_space + number < 64:
                self.player2_space = self.player2_space + number
            if self.player2_space == 9:
                self.player2_space = 16
            if self.player2_space not in [4, 8, 13, 18, 23, 27]:
                self.current_player = self.player1

    def get_last_dice_roll(self) -> Optional[Tuple[int, int]]:
        """Returns either None or a pair of die rolls, like (2, 6)"""
        if self.d1 is None:
            return None
        else:
            return self.d1, self.d2
        
    def is_over(self) -> bool:
        """Returns True if game is over."""
        if self.player1_space == 63 or self.player2_space == 63:
            return True
        else:
            return False
    
    def get_winner(self) -> Optional[str]:
        """Returns None (if the game is not over) or the name of the winner"""
        if self.is_over():
            if self.get_player1_space() == 63:
                return self.player1
            else:
                return self.player2
        else:
            return None

    
    