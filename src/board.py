from .config import width, height, pre_built_board
from .ships import Ships

class Board:

    def __init__(self):
        self.width = width
        self.height = height
        self.initial_board = [[0 for i in range(self.width)] for j in range(self.height)]
        self.ships = Ships()

    def print_board(self):
        print(self.initial_board)
        for _height in self.initial_board:
            print(_height)

    def setup_board(self, test=False):
        if test:
            return pre_built_board
        for ship in self.ships:
            start_x = self.ships[ship]['start'][0]
            start_y = self.ships[ship]['start'][1]
            end_x = self.ships[ship]['end'][0]
            end_y = self.ships[ship]['end'][1]

            # if end_x - start_x != 0:
            for x,y in enumerate(self.initial_board):
                if x == start_x and y == start_y:
                    self.initial_board[x][y] == 1


    # @staticmethod
    def set_ship(self):
        for i, x in enumerate(self.initial_board):
            for y in x:
                print(self.initial_board[i][y])





