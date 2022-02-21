import os
import sys
from unittest import TestCase

from checkers.items import GameBoard, Player

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# @pytest.fixture
# def two_player_game():
#     """Test a two player game"""
#     return Game()


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_two_player_game(self):
        game = GameBoard(total_rows=8, total_cols=8)
        assert isinstance(game, GameBoard)

        player_rafael = Player(name="Rafael")
        assert isinstance(player_rafael, Player)

