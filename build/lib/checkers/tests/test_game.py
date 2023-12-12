import pytest
from checkers.board import GameBoard
from checkers.player import Player
from checkers.game import Game

def test_game():
    game = Game()
    assert isinstance(game, Game)
