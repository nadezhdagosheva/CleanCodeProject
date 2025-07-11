from models.player import Player

class ShipGame:
    def __init__(self):
        self._player_turn = "first"
        self._player_1 = Player()
        self._player_2 = Player()
        self._state = "UNFINISHED"
        self._letters = {chr(i + 65): i for i in range(10)}
        self._last_message = None

    def get_last_message(self):
        return self._last_message

    def _set_message(self, message):
        self._last_message = message

    def _get_players(self, player):
        return (self._player_1, self._player_2) if player == "first" else (self._player_2, self._player_1)

    def _is_valid_position(self, x, y):
        return 0 <= x < 10 and 0 <= y < 10

    def place_ship(self, player, ship_name, coord, orientation):
        self._set_message(None)
        current, _ = self._get_players(player)

        if ship_name in current.get_ships():
            self._set_message("Ship already placed.")
            return False

        x, y = self._parse_coordinates(coord)
        if not self._is_valid_position(x, y):
            self._set_message("Invalid position.")
            return False

        current.add_ship(ship_name)
        ship = current.get_ship(ship_name)
        board = current.get_board()

        dx, dy = (1, 0) if orientation == 'C' else (0, 1)
        locations = [(x + i * dx, y + i * dy) for i in range(ship.get_length())]

        if any(not self._is_valid_position(px, py) or board[px][py] == 'X' for px, py in locations):
            current.remove_ship(ship_name)
            self._set_message("Ship overlaps or is off-board.")
            return False

        for px, py in locations:
            board[px][py] = 'X'
            ship.add_location((px, py))

        return True

    def fire_torpedo(self, player, coord):
        self._set_message(None)

        if self._state != "UNFINISHED":
            self._set_message("Game already finished.")
            return 

        if player != self._player_turn:
            self._set_message("Not your turn.")
            return 

        current, opponent = self._get_players(player)
        x, y = self._parse_coordinates(coord)
        if not self._is_valid_position(x, y):
            self._set_message("Invalid target.")
            return False

        opp_board = opponent.get_board()

        if opp_board[x][y] == 'X':
            if (x, y) not in current.get_hits():
                current.add_hit((x, y))
            hit = True
        else:
            current.add_miss((x, y))
            hit = False

        self._update_ship_statuses(opponent, current)
        self._check_game_state(opponent, player)

        self._player_turn = "second" if player == "first" else "first"
        return hit

    def _update_ship_statuses(self, opponent, current):
        for ship in opponent.get_ships().values():
            for pos in ship.get_location():
                if pos in current.get_hits():
                    ship.reduce_length()
                    current.remove_hit(pos)
            if ship.get_length() <= 0:
                ship.set_status("sunk")

    def _check_game_state(self, opponent, shooter):
        if all(ship.get_status() == "sunk" for ship in opponent.get_ships().values()):
            self._state = "PLAYER1_WON" if shooter == "first" else "PLAYER2_WON"
            self._set_message(f"{shooter.capitalize()} player won!")

    def _parse_coordinates(self, coord):
        letter = coord[0].upper()
        x = self._letters.get(letter, -1)
        try:
            y = int(coord[1:]) - 1
        except ValueError:
            y = -1
        return x, y

    def get_num_ships_remaining(self, player):
        current, _ = self._get_players(player)
        return sum(1 for s in current.get_ships().values() if s.get_status() != "sunk")

    def get_current_state(self):
        return self._state
