from checkers.game import Game
import pytest


@pytest.fixture
def two_player_game():
    """Test a two player game"""
    return Game()
