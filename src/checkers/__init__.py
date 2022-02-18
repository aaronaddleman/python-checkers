"""The checkers module."""

from items import GameBoard


class Checkers:
    """Start a game of checkers."""

    def __init__(self):
        """Start the game of checkers."""
        game = GameBoard()
        print(game)
