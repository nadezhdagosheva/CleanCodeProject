# Author: Donald Reniff
# Github username: dreniff3
# Description: This module contains the classes necessary for instantiating a simulated game of Battleship.
from tkinter import messagebox


class Ship:
    """ Represents a ship.

    Attributes:
        _name (str): The name of the ship.
        _length (int): The length of the ship.
        _location (list): The (x, y) coordinates the ship occupies on the player's game board.
        _status (str): If all of the ship's (x, y) coordinates have been hit by an enemy's torpedoes, the ship status
            is "sunk", otherwise it is "live".
    """

    def __init__(self, name):
        """ The constructor of the Ship class. Sets all data members to their initial values. """
        self._name = name
        if name == 'carrier':
            self._length = 5
        if name == 'battle-ship':
            self._length = 4
        if name == 'cruiser':
            self._length = 3
        if name == 'submarine':
            self._length = 3
        if name == 'destroyer':
            self._length = 2
        self._location = []
        self._status = "live"

    def get_name(self):
        """ Gets the name of the ship. """
        return self._name

    def get_length(self):
        """ Gets the length of the Ship. """
        return self._length

    def change_length(self, length):
        """
        Changes the value of the length data member of the Ship.
        :param length: The amount to change the length by.
        """
        self._length += length

    def add_location(self, position):
        """
        Takes as a parameter the (x, y) position the ship occupies on the game board and adds that tuple to the list
        of ship positions.

        :param position: The (x, y) position the ship occupies on the game board.
        """
        self._location.append(position)

    def get_location(self):
        """ Gets the list of (x, y) positions the Ship object occupies on the player's board. """
        return self._location

    def change_status(self, status):
        """
        Changes the status of the ship to the string provided.
        :param status: A string, what to change the ship's status to.
        """
        self._status = status

    def get_status(self):
        """ Gets the Ship object's current status. """
        return self._status


class Player:
    """ Represents a player.

    Attributes:
        _turn (str): Either "first" or "second", designating which turn the Player can legally take.
        _ships (dict): The player's collection of Ship objects.
        _hits (list): The (x, y) positions of each hit the Player has made on their opponent's ships.
        _misses (list): The torpedo misses recorded as (x, y) positions.
        _board (list): The player's 10x10 game board represented as a list of ten lists ten strings long.
        _grid (list): The printable board of hits and misses.
    """

    def __init__(self, turn):
        """ The constructor of the Player class. Initializes all data members to their initial values. """
        self._turn = turn
        self._ships = {}
        self._hits = []
        self._misses = []
        self._board = [[' '] * 10 for i in range(10)]
        self._grid = [[' '] * 10 for i in range(10)]

    def add_ships(self, name):
        """
        Takes as a parameter the name of a ship. Instantiates a Ship object using the provided name and adds that ship
        to the collection of the Player's ships.

        :param name: The name of the ship to add.
        """
        self._ships[name] = Ship(name)

    def remove_ship(self, name):
        """
        Removes a ship specified by the length parameter from the Player's collection of ships.

        :param name: The string name of the ship to remove.
        """
        if name in self._ships:
            del self._ships[name]
            return

    def get_ships(self):
        """ Gets the Player's collection of ships. """
        return self._ships

    def get_board(self):
        """ Gets the Player's board. """
        return self._board

    def get_grid(self):
        """ Gets the Player's grid, where misses and hits are recorded. """
        return self._grid

    def add_hits(self, position):
        """
        Adds a hit to the list of hits.
        :param position: A tuple, the (x, y) position where the hit was made on the enemy's board.
        """
        self._hits.append(position)

    def remove_hits(self, position):
        """
        Removes a hit already used by ShipGame fire_torpedo method for decrementing a ship's length.
        :param position: The tuple (x, y) position of a torpedo hit on an opponent ship.
        """
        self._hits.remove(position)

    def get_hits(self):
        """ Gets the list of hits. """
        return self._hits

    def add_misses(self, position):
        """
        Adds a miss to the list of misses.
        :param position: A tuple, the (x, y) position where the torpedo missed on the enemy's board.
        """
        self._misses.append(position)

    def get_misses(self):
        """ Gets the list of misses. """
        return self._misses


class ShipGame:
    """ Represents a game of Battleship.

    Attributes:
        _player_turn (str): The player whose turn it is.
        _player_1 (Player): The Player object representing player_1.
        _player_2 (Player): The Player object representing player_2.
        _letters_to_numbers (dict): A collection of key-value pairs for translating ship and torpedo coordinates into
            (x, y) positions on a player's board.
    """

    def __init__(self):
        """
        The constructor of the ShipGame class. Takes no parameters and initializes all data members to their initial
        values.
        """
        self._player_turn = "first"
        self._player_1 = Player("first")
        self._player_2 = Player("second")
        self._letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        self._current_state = 'UNFINISHED'

    def place_ship(self, player, ship, coordinates, orientation):
        """
        Places a ship on a player's grid at a designated starting-coordinate.
        If a ship does not fit entirely on that player's grid, or if it would overlap any previously placed ships
        on that player's grid, the ship is not added and the method returns False.

        :param player: The player placing the ship, either "first" or "second".
        :param ship: The ship being placed.
        :param coordinates: The letter-and-number coordinates of the closest square to 'A1' that the ship will occupy.
        :param orientation: The ship's orientation, either "R" if the ship occupies squares in a row, or "C" if it
            occupies squares in a column.
        :returns Boolean: True if the ship can be placed on the board, False otherwise.
        """
        if player == "first":
            player_obj = self._player_1
        else:
            player_obj = self._player_2

        board = player_obj.get_board()
        ships = player_obj.get_ships()

        if ship not in ships:
            player_obj.add_ships(ship)
            ship_obj = player_obj.get_ships()[ship]
            ship_name = ship_obj.get_name()
            ship_length = ship_obj.get_length()
        else:
            messagebox.showerror("Battleship", "Choose a different ship.")
            return False

        # translate coordinates into (x, y) position
        letter = coordinates[0]
        x = self._letters_to_numbers[letter]
        y = int(coordinates[1:3]) - 1
        # if the ship does not fit on board
        if x < 0 or y < 0 or x >= 10 or y >= 10:
            player_obj.remove_ship(ship_name)
            messagebox.showerror("Battleship", "Choose a position on the board.")
            return False
        # if the ship would overlap with another ship
        if board[x][y] == 'X':
            player_obj.remove_ship(ship_name)
            messagebox.showerror("Battleship", "Place the ship in an empty position.")
            return False
        board[x][y] = 'X'
        ship_obj.add_location((x, y))
        # place the rest of the ship on the board according to orientation provided
        # if the squares of the ship occupy the same row
        if orientation == 'R':
            for i in range(1, ship_length):
                temp_y = y + i
                if x < 0 or temp_y < 0 or x >= 10 or temp_y >= 10:
                    player_obj.remove_ship(ship_name)
                    messagebox.showerror("Battleship", "Choose a position on the board.")
                    return False
                # if the ship would overlap with another ship
                elif board[x][temp_y] == 'X':
                    player_obj.remove_ship(ship_name)
                    messagebox.showerror("Battleship", "Place the ship in an empty position.")
                    return False
                else:
                    board[x][temp_y] = 'X'
                    ship_obj.add_location((x, temp_y))
            return True
        elif orientation == 'C':
            for i in range(1, ship_length):
                temp_x = x + i
                if temp_x < 0 or y < 0 or temp_x >= 10 or y >= 10:
                    player_obj.remove_ship(ship_name)
                    messagebox.showerror("Battleship", "Choose a position on the board.")
                    return False
                # if the ship would overlap with another ship
                elif board[temp_x][y] == 'X':
                    player_obj.remove_ship(ship_name)
                    messagebox.showerror("Battleship", "Place the ship in an empty position.")
                    return False
                else:
                    board[temp_x][y] = 'X'
                    ship_obj.add_location((temp_x, y))
            return True

    def fire_torpedo(self, player, target_coordinates, button=None):
        """
        Method for firing a torpedo at a specified target square. If it's not that player's turn, or if the game
        has already been won, it returns False. Otherwise, it records the move, updates whose turn it is, updates
        the current state (if this turn sank the opponent's final ship), and returns True.

        :param player: The player firing the torpedo, either 'first' or 'second'.
        :param target_coordinates: The coordinates of the target square, e.g. 'B7'.
        :param button: The button associated with the target_coordinates to change.
        :returns Boolean: True if it is that player's turn and the game is not over, False otherwise.
        """
        # if the game has already been won
        if self._current_state != 'UNFINISHED':
            return False

        # if it's not this player's turn
        if player != self._player_turn:
            messagebox.showerror("Battleship", "Not your turn.")
            return False

        if player == "first":
            player_obj = self._player_1
            opponent_obj = self._player_2
        else:
            player_obj = self._player_2
            opponent_obj = self._player_1

        letter = target_coordinates[0]
        x = self._letters_to_numbers[letter]
        # this slice allows for '10'
        y = int(target_coordinates[1:3]) - 1
        opponent_board = opponent_obj.get_board()
        if x < 0 or y < 0 or x >= 10 or y >= 10:
            messagebox.showerror("Battleship", "Choose a position on the board.")
            return False
        if opponent_board[x][y] == 'X':
            if (x, y) not in player_obj.get_hits():
                player_obj.add_hits((x, y))
                if button:
                    button['text'] = "X"
                    button.config(bg='red')
        else:
            player_obj.add_misses((x, y))
            if button:
                button['text'] = "O"
                button.config(bg='blue')

        opponent_ships = opponent_obj.get_ships().values()
        for ship in opponent_ships:
            for position in ship.get_location():
                if position in player_obj.get_hits():
                    ship.change_length(-1)
                    # remove recorded hits already used to decrement length of ship so they are not counted multiple
                    # times as the loop iterates
                    player_obj.remove_hits(position)
            if ship.get_length() <= 0:
                ship.change_status("sunk")

            if ship.get_status() != "sunk":
                if player_obj == self._player_1:
                    self._player_turn = "second"
                    return True
                else:
                    self._player_turn = "first"
                    return True
            else:
                # a player wins and the game ends when all of a player's ships are "sunk"
                if all(ship.get_status() == "sunk" for ship in opponent_ships):
                    if player_obj == self._player_1:
                        self._current_state = 'FIRST_WON'
                        messagebox.showinfo('Battleship', 'Player1 won!')
                        return True
                    else:
                        self._current_state = 'SECOND_WON'
                        messagebox.showinfo('Battleship', 'Player2 won!')
                        return True

    def get_current_state(self):
        """ Gets the current state of the game. """
        return self._current_state

    def get_num_ships_remaining(self, player):
        """
        Returns how many ships the specified player has left.

        :param player: The player, either 'first' or 'second'.
        :returns count: The number of ships the specified player has left.
        """
        if player == "first":
            player_obj = self._player_1
        else:
            player_obj = self._player_2

        count = 0
        for ship in player_obj.get_ships().values():
            if ship.get_status() != "sunk":
                count += 1
            else:
                continue
        return count

    def print_board(self, player):
        """ Prints the 10x10 grid showing the Player's ship placements. """
        if player == "first":
            player_obj = self._player_1
        else:
            player_obj = self._player_2
        board = player_obj.get_board()
        print(" ", " ".join("123456789" + "10"))
        for letter, row in zip("ABCDEFGHIJ", board):
            print(letter, " ".join(row))