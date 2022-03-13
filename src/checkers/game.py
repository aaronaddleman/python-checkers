"""Create a game to play checkers."""
from checkers.board import GameBoard
from checkers.player import Player

class Game:
    """Start a game."""

    def __init__(self, total_players=2, board_size=8):
        """Set a game up with players and board_size."""
        self.gameboard = GameBoard()
        self.gameboard.build_board()
