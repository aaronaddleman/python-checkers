from checkers.board import GameBoard
from checkers.player import Player
from checkers.game import Game


def test_instances():
    game = Game()
    board = GameBoard()
    player = Player()
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
    exp_output = """
|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b
|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w
|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b|    w|  ϕ b
|    b|    w|    b|    w|    b|    w|    b|    w
|    w|    b|    w|    b|    w|    b|    w|    b
|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w
|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b
|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w|  ⦁ b|    w
    """
    assert exp_output == ret_output


def test_starting_game():
    return True
