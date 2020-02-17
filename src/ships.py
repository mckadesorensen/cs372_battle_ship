from .config import ships


class Ships:

    def __init__(self):
        self.ships = ships
        self.remaining_ships = self.total_ships()

    def total_ships(self):
        total = 0
        for ship in self.ships:
            total += self.ships[ship]['total']
        return total

    def __print_total__(self):
        print(self.total_ships)

    # TODO: Add a test fucntion
    def remove_a_ship(self):
        self.remaining_ships -= 1
