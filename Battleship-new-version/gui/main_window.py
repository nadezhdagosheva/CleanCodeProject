# gui/main_window.py

import os
from tkinter import *
from tkinter import messagebox
from game.ship_game import ShipGame
from gui.components import build_board_frames, build_ship_placement_controls, build_status_panel, build_grids
from gui.events import place_ship, show_remaining_ships, handle_grid_click

class BattleshipGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("750x550")
        self.root.title('Battleship')

        icon_path = os.path.abspath("battleship-icon.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.game = ShipGame()

        self.player_turn_var = StringVar(value='first')
        self.ship_choice_var = StringVar(value="carrier")
        self.orientation_var = StringVar(value="R")
        self.status_player = StringVar(value='first')

        self.position_entry = None
        self.ships_frame = None
        self.status_label = None
        self.player_buttons = {
            "first": {},
            "second": {}
        }

        self.build_gui()

    def build_gui(self):
        build_board_frames(self)
        build_ship_placement_controls(self)
        build_status_panel(self)
        build_grids(self, "first")
        build_grids(self, "second")

    def on_grid_click(self, x, y, shooter, target):
        handle_grid_click(self, x, y, shooter, target)


if __name__ == '__main__':
    root = Tk()
    app = BattleshipGUI(root)
    root.mainloop()
