class Ship:
    def __init__(self, name):
        self._name = name
        self._length = self._get_length_by_name(name)
        self._location = []
        self._status = "live"

    def _get_length_by_name(self, name):
        lengths = {
            'carrier': 5,
            'battle-ship': 4,
            'cruiser': 3,
            'submarine': 3,
            'destroyer': 2
        }
        return lengths.get(name, 0)

    def add_location(self, position):
        self._location.append(position)

    def get_location(self):
        return self._location

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def reduce_length(self):
        self._length -= 1

    def get_length(self):
        return self._length
