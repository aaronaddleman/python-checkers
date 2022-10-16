from checkers.board import GameBoard
from checkers.player import Player
from checkers.game import Game
import pytest


@pytest.fixture
def game():
    game = Game()
    return game


@pytest.fixture
def board():
    board = GameBoard()
    return board


@pytest.fixture
def player():
    player = Player()
    return player


@pytest.fixture
def playerWhite(player):
    playerWhite = player(color="white", name="Mack")
    return playerWhite


@pytest.fixture
def playerBlack(player):
    playerBlack = player(color="black", name="Charlie")
    return playerBlack


def test_instances(game, board, player):
    assert isinstance(game, Game)
    assert isinstance(board, GameBoard)
    assert isinstance(player, Player)


def test_creating_game():
    gameboard = GameBoard()
    playerWhite = Player(color="white", name="Vim")
    playerBlack = Player(color="black", name="Emacs")
    gameboard.build_board()
    gameboard.add_player_pieces(player_white=playerWhite,
                                player_black=playerBlack)
    exp_data = {'num_of_black_pieces': 12,
                'num_of_player_pieces': 24,
                'num_of_white_pieces': 12}
    assert exp_data == gameboard.stats()


def test_printing_board():
    playerWhite = Player(color="white", name="Vim")
    playerBlack = Player(color="black", name="Emacs")
    board = GameBoard()
    board.build_board()
    board.add_player_pieces(player_white=playerWhite,
                            player_black=playerBlack)
    ret_output = board.print_board()
    exp_output = ""
    exp_output += "|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b"
    exp_output += "|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w"
    exp_output += "|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b"
    exp_output += "|    b|    w|    b|    w|    b|    w|    b|    w"
    exp_output += "|    w|    b|    w|    b|    w|    b|    w|    b"
    exp_output += "|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w"
    exp_output += "|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b"
    exp_output += "|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w"
    assert exp_output == ret_output


def test_check_space_is_occupied():
    playerWhite = Player(color="white", name="Vim")
    playerBlack = Player(color="black", name="Emacs")
    board = GameBoard()
    board.build_board()
    board.add_player_pieces(player_white=playerWhite,
                            player_black=playerBlack)
    space_status = board.check_space_status(row=4, col=4, mode="is_occupied")
    assert space_status is False


def test_finding_move_for_black():
    playerWhite = Player(color="white", name="Vim")
    playerBlack = Player(color="black", name="Emacs")
    board = GameBoard()
    board.build_board()
    board.add_player_pieces(player_white=playerWhite,
                            player_black=playerBlack)
    moves = board.possible_moves(row=6, col=1)
    assert moves is ["1"]



def test_starting_game():
    return True
