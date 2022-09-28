"""Create a game to play checkers."""
from checkers.board import GameBoard
from checkers.player import Player


class Game:
    """Start a game."""

    def __init__(self, total_players=2, board_size=8):
        """Set a game up with players and board_size."""
        self.gameboard = GameBoard()
        self.gameboard.build_board()

    def start_game(self):
        """Start the game and see who wins."""
        # add players
        player1black = Player(color="black")
        player2white = Player(color="white")
        self.gameboard.add_player_pieces(player_black=player1black, player_white=player2white)
        # print the board
        self.gameboard.print_board()
