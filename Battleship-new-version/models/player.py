from models.ship import Ship

class Player:
    def __init__(self):
        self._ships = {}
        self._hits = []
        self._misses = []
        self._board = [[' '] * 10 for _ in range(10)]

    def add_ship(self, ship_name):
        self._ships[ship_name] = Ship(ship_name)

    def get_ship(self, ship_name):
        return self._ships.get(ship_name)

    def remove_ship(self, ship_name):
        if ship_name in self._ships:
            del self._ships[ship_name]

    def get_ships(self):
        return self._ships

    def get_board(self):
        return self._board

    def add_hit(self, pos):
        self._hits.append(pos)

    def add_miss(self, pos):
        self._misses.append(pos)

    def get_hits(self):
        return self._hits

    def remove_hit(self, pos):
        if pos in self._hits:
            self._hits.remove(pos)
