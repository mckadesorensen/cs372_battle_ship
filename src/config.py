width, height = 8, 8
ships = {"ship_size_four":  {"total": 1, "length": 4, "start": (0, 0), "end": (0, 3)},
         "ship_size_three": {"total": 1, "length": 3, "start": (2, 5), "end": (4, 5)},
         "ship_size_two":   {"total": 1, "length": 2, "start": (6, 2), "end": (6, 3)},
         "ship_size_one":   {"total": 1, "length": 1, "start": (3, 1), "end": (3, 1)},
         "ship_size_one_copy":   {"total": 1, "length": 1, "start": (1, 7), "end": (1, 7)}}

# TODO: Remove this later
pre_built_board = [[1, 1, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]]

# Note this should match the sum of the ships dictionary
total_ships = 5
