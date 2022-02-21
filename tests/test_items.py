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

