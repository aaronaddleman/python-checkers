"""All items that are part of the checkers game."""


class GameBoard:
    """Create a game board."""

    def __init__(self, x=1, y=1):
        """Initialize the board with a size."""
        self.x = x
        self.y = y


class Player:
    """Create a player."""

    def __init__(self, name=False):
        """Create a player to participate in the game."""
        self.name = name


