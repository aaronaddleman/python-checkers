"""Create a game to play checkers."""
from .items import GameBoard, Player


class Game:
    """Start a game."""

    def __init__(self, total_players=2, board_size=8):
        """Set a game up with players and board_size."""
        self.total_players = total_players
        self.board_size = GameBoard(x=board_size, y=board_size)
        self.players = []
        self.turn_history = []

    def draw_board(self):
        print("Drawing the board")

    def player_turn(self):
        return {"player_name": "harry",
                "translation": {"src": {"row": 2, "col": 1},
                                "dst": {"row": 3, "col": 2}}}

    def player_takes_turn(self):
        self.turn_history.append(self.player_turn())
