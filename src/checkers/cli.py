"""
Checkers game.

Usage:
  pycheckers startgame

Options:
  -h --help    Show this screen.
  --version    Show version.
"""
from docopt import docopt
from .player import Player
from .board import GameBoard
from .game import Game


def main():
    """Entry point for the cli interface of checkers."""
    args = docopt(__doc__)
    if args['startgame']:
        playerWhite = Player(color="white", name="FirstPlayer")
        playerBlack = Player(color="black", name="SecondPlayer")
        board = GameBoard()
        board.build_board()
        board.add_player_pieces(
            player_white=playerWhite,
            player_black=playerBlack)
        board.print_board()
        gameActive = True
        while gameActive:
            print("Action: ")
            selected_answer = input()
            print(f"You selected {selected_answer}")
            if selected_answer == "quit":
                gameActive = False
                break
            if selected_answer == "print":
                board.print_board()


if __name__ == '__main__':
    main()
