from src.board import Board
from src.config import WIDTH, HEIGHT
from src.ships import Ships

import pytest


# Board tests below
def test_board_size():
    board = Board()
    assert board.width == WIDTH
    assert board.height == HEIGHT

def test_setup_board():
    _board = Board()
    assert _board.setup_board(True) == [[1, 1, 1, 1, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 1],
                                        [0, 0, 0, 0, 0, 1, 0, 0],
                                        [0, 1, 0, 0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 1, 1, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0]]



# def test_board_build():
#     board = Board(width, height)
#     initial_board = [[0 for i in range(width)] for j in range(height)]
#     assert board.set_board(1,2,2,'h') # unfinished


# Ship tests below
def test_ship_count():
    _ships = Ships()
    assert _ships.total_ships() == 5
