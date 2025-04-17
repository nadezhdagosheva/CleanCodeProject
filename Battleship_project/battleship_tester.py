import unittest
from ship_game_classes import ShipGame


class TestShipGame(unittest.TestCase):
    """ Contains unit tests for ship_game_classes module. """

    def test_game_instantiation(self):
        """ Tests instantiation of a ShipGame object. """
        s = ShipGame()
        self.assertIsInstance(s, ShipGame)

    def test_place_ship_1(self):
        """
        Tests if a ship is placed in the right location on the player's board and is also placed in that
        player's collection.
        """
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F8', 'R')
        self.assertEqual('destroyer' in s._player_1.get_ships(), True)
        self.assertEqual(s._player_1.get_ships()['destroyer'].get_location(), [(5, 7), (5, 8)])

    def test_place_ship_2(self):
        """ Test that a ship placed off the board is not counted. """
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F8', 'R')
        s.place_ship("first", 'carrier', 'J9', 'R')
        self.assertEqual(s.get_num_ships_remaining("first"), 1)

    def test_place_ship_3(self):
        """ Test that a ship placed on positions already occupied is not counted. """
        s = ShipGame()
        s.place_ship("first", 'carrier', 'C1', 'R')
        s.place_ship("first", 'battle-ship', 'B2', 'C')
        self.assertEqual(s.get_num_ships_remaining("first"), 1)

    def test_place_ship_all_1(self):
        """ Test that a player can place all five ships on the board. """
        s = ShipGame()
        s.place_ship("first", 'carrier', 'A1', 'R')
        s.place_ship("first", 'battle-ship', 'B1', 'R')
        s.place_ship("first", 'cruiser', 'C3', 'R')
        s.place_ship("first", 'submarine', 'D1', 'C')
        s.place_ship("first", 'destroyer', 'E5', 'C')
        self.assertEqual(s.get_num_ships_remaining("first"), 5)

    def test_place_ship_all_2(self):
        """ Test that both players can place all five ships on their respective boards. """
        s = ShipGame()
        s.place_ship("first", 'carrier', 'A1', 'R')
        s.place_ship("first", 'battle-ship', 'B1', 'R')
        s.place_ship("first", 'cruiser', 'C3', 'R')
        s.place_ship("first", 'submarine', 'D1', 'C')
        s.place_ship("first", 'destroyer', 'E5', 'C')
        s.place_ship("second", 'carrier', 'A1', 'R')
        s.place_ship("second", 'battle-ship', 'B1', 'R')
        s.place_ship("second", 'cruiser', 'C3', 'R')
        s.place_ship("second", 'submarine', 'D1', 'C')
        s.place_ship("second", 'destroyer', 'E5', 'C')
        self.assertEqual(s.get_num_ships_remaining("first"), 5)
        self.assertEqual(s.get_num_ships_remaining("second"), 5)

    def test_player_turn_1(self):
        """ Test that player 1 takes the first turn. """
        s = ShipGame()
        self.assertEqual(s.fire_torpedo("second", 'F5'), False)

    def test_player_turn_2(self):
        """ Test that player 1 can take the first turn. """
        s = ShipGame()
        s.place_ship("second", 'destroyer', 'F5', 'R')
        self.assertEqual(s.fire_torpedo("first", 'F5'), True)

    def test_take_turns(self):
        """ Test that turn order changes as players make legal moves. """
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F8', 'R')
        s.place_ship("second", 'destroyer', 'C5', 'C')
        s.fire_torpedo("first", 'I5')
        self.assertEqual(s._player_turn, "second")
        s.fire_torpedo("second", 'A1')
        self.assertEqual(s._player_turn, "first")

    # def test_torpedo(self):
    #     """ Test when a torpedo hits a ship position and when a torpedo misses. """
    #     s = ShipGame()
    #     s.place_ship("first", 'submarine', 'A1', 'C')
    #     s.place_ship("second", 'battle-ship', 'A1', 'R')
    #     s.fire_torpedo("first", 'F9')
    #     s.fire_torpedo("second", 'B1')
    #     self.assertEqual(s._player_1.get_misses(), [(5, 8)])
    #     self.assertEqual(s._player_2.get_hits(), [(1, 0)])

    def test_sink_ship(self):
        """ Test if a ship has sunk when all its positions have been hit by torpedoes. """
        s = ShipGame()
        s.place_ship("second", 'destroyer', 'F5', 'R')
        s.fire_torpedo("first", 'F5')
        s._player_turn = "first"
        s.fire_torpedo("first", 'F6')
        self.assertEqual(s._player_2.get_ships()['destroyer'].get_status(), "sunk")

    def test_current_state(self):
        """ Test that the game starts unfinished. """
        s = ShipGame()
        self.assertEqual(s.get_current_state(), "UNFINISHED")

    def test_player_1_win(self):
        """ Test that player 1 wins when all player 2 ships are sunk. """
        s = ShipGame()
        s.place_ship("second", 'destroyer', 'F5', 'R')
        s.fire_torpedo("first", 'F5')
        s._player_turn = "first"
        s.fire_torpedo("first", 'F6')
        self.assertEqual(s.get_current_state(), 'FIRST_WON')

    def test_player_2_win(self):
        """ Test that player 2 wins when all player 1 ships are sunk. """
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F5', 'R')
        s._player_turn = "second"
        s.fire_torpedo("second", 'F5')
        s._player_turn = "second"
        s.fire_torpedo("second", 'F6')
        self.assertEqual(s.get_current_state(), 'SECOND_WON')


if __name__ == "__main__":
    unittest.main(exit=False)