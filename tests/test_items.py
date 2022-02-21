import os
import sys
from unittest import TestCase

import pytest
from checkers.items import GameBoard, Player

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def gameboard():
    """Test a two player game"""
    game = GameBoard(total_rows=8, total_cols=8)
    return game

def test_gameboard(gameboard):
    assert isinstance(gameboard, GameBoard)

