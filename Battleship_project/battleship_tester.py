import unittest
from ship_game_classes import ShipGame


class TestShipGame(unittest.TestCase):
    def test_game_instantiation(self):
        s = ShipGame()
        self.assertIsInstance(s, ShipGame)

    def test_place_ship_valid(self):
        s = ShipGame()
        self.assertTrue(s.place_ship("first", "destroyer", "A1", "R"))

    def test_place_ship_overlap(self):
        s = ShipGame()
        s.place_ship("first", "carrier", "A1", "R")
        self.assertFalse(s.place_ship("first", "battle-ship", "A1", "R"))
        self.assertEqual(s.get_last_message(), "Ship overlaps or is off-board.")

    def test_torpedo_hit_and_miss(self):
        s = ShipGame()
        s.place_ship("second", "carrier", "A1", "R")
        self.assertTrue(s.fire_torpedo("first", "A1"))
        s._player_turn = "first"
        self.assertFalse(s.fire_torpedo("first", "J10"))

    def test_victory(self):
        s = ShipGame()
        s.place_ship("second", "destroyer", "A1", "R")
        s.fire_torpedo("first", "A1")
        s._player_turn = "first"
        s.fire_torpedo("first", "A2")
        self.assertEqual(s.get_current_state(), "FIRST_WON")
        self.assertEqual(s.get_last_message(), "First won!")


if __name__ == '__main__':
    unittest.main()
