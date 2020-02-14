from src.main import test
from src.board import Board
from src.config import width, height

import pytest


def test_board_size():
    board = Board(width,height)
    assert board.width == width
    assert board.height == height


def test_board_build():
    board = Board(width, height)
    initial_board = [[0 for i in range(width)] for j in range(height)]
    assert board.set_board(1,2,2,'h') # unfinished