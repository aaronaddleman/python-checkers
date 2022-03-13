"""Create and manage a player for checkers game"""
PLAYER_WHITE = "ϕ"
PLAYER_BLACK = "⦁"


class Player:
    """Create a player."""

    def __init__(self, color=False, name=False):
        """Create a player to participate in the game."""
        self.name = name
        self.color = color
        self.set_symbol()

    def set_symbol(self):
        """Set the symbol for player based on the color"""
        if self.color == "white":
            self.player_symbol = PLAYER_WHITE
        if self.color == "black":
            self.player_symbol = PLAYER_BLACK

    def stats(self):
        """Print the players status."""
        return {
            "player": self,
            "points": 0
        }
