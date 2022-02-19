"""Create a game to play checkers."""
from .items import GameBoard, Player


class Game:
    """Start a game."""

    def __init__(self, total_players=2, board_size=5):
        """Set a game up with players and board_size."""
        self.total_players = total_players
        self.board_size = GameBoard(x=board_size, y=board_size)

    def draw_board(self):
        print("Drawing the board")
