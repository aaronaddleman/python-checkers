PLAYER_WHITE = "lambda"
PLAYER_BLACK = "theta"

class Player:
    """Create a player."""

    def __init__(self, color=False, name=False):
        """Create a player to participate in the game."""
        self.name = name
        if color == "white":
            self.player_symbol = "w"
        if color == "black":
            self.player_symbol = "b"

    def stats(self):
        """Print the players status."""
        return {"points": 0}
