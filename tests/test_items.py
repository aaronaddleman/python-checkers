import os
import sys
from unittest import TestCase

import pytest
from checkers.items import GameBoard, Player

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def gameboard():
    """Test gameboard properties"""
    game = GameBoard(total_rows=8, total_cols=8)
    return game

@pytest.fixture
def players():
    """Create some players"""
    player_black = Player(color="black", name="Beta")
    player_white = Player(color="white", name="Lambda")
    players = (player_black, player_white)
    return players

def test_gameboard(gameboard):
    assert isinstance(gameboard, GameBoard)
    gameboard.build_board()
    # get the color of a squre
    white_square = gameboard.grid[0][0].get('color')
    # get the color of a squre
    black_square = gameboard.grid[3][0].get('color')
    # test the color value of the squares of
    # what they should be based on the size of the board
    assert white_square == "white"
    assert black_square == "black"
    # add pieces to the board
    gameboard.add_player_pieces()
    # count things on the board
    stats = gameboard.stats()
    # we should start out with 24 pieces on the board
    assert stats['num_of_player_pieces'] == 24
    # we should have 12 black
    assert stats['num_of_black_pieces'] == 12
    # we should have 12 white
    assert stats['num_of_white_pieces'] == 12

def test_players(players):
    for player in players:
        assert isinstance(player, Player)
