import os
from tkinter import *
from tkinter import messagebox
from ship_game_classes import ShipGame


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
        self.build_board_frames()
        self.build_ship_placement_controls()
        self.build_status_panel()
        self.build_grids("first")
        self.build_grids("second")

    def build_board_frames(self):
        self.frame_player1 = LabelFrame(self.root, text="Player1", padx=10, pady=10)
        self.frame_player1.grid(row=0, column=0, padx=10, pady=10)

        self.frame_player2 = LabelFrame(self.root, text="Player2", padx=10, pady=10)
        self.frame_player2.grid(row=0, column=1, padx=10, pady=10)

    def build_ship_placement_controls(self):
        controls_frame = LabelFrame(self.root, text="Place Ship", padx=15, pady=15)
        controls_frame.grid(row=1, column=0, padx=30, pady=20)

        Radiobutton(controls_frame, text="Player1", variable=self.player_turn_var, value='first').grid(row=0, column=0)
        Radiobutton(controls_frame, text="Player2", variable=self.player_turn_var, value='second').grid(row=0, column=1)

        OptionMenu(controls_frame, self.ship_choice_var, "carrier", "battle-ship", "cruiser", "submarine", "destroyer").grid(row=1, column=0)

        self.position_entry = Entry(controls_frame, width=5)
        self.position_entry.grid(row=1, column=1)

        Radiobutton(controls_frame, text="Row", variable=self.orientation_var, value='R').grid(row=1, column=2)
        Radiobutton(controls_frame, text="Col", variable=self.orientation_var, value='C').grid(row=1, column=3)

        Button(controls_frame, text="Place the ship", command=self.place_ship).grid(row=2, column=3)

    def build_status_panel(self):
        self.ships_frame = LabelFrame(self.root, text="Ships Remaining", padx=15, pady=15)
        self.ships_frame.grid(row=1, column=1, padx=10, pady=10)

        Radiobutton(self.ships_frame, text="Player1", variable=self.status_player, value='first').grid(row=0, column=0)
        Radiobutton(self.ships_frame, text="Player2", variable=self.status_player, value='second').grid(row=0, column=1)

        Button(self.ships_frame, text="Show ships", command=self.show_remaining_ships).grid(row=1, column=0)
        self.status_label = Label(self.ships_frame, text="")
        self.status_label.grid(row=1, column=1)

    def place_ship(self):
        player = self.player_turn_var.get()
        ship = self.ship_choice_var.get().strip()
        pos = self.position_entry.get()
        orientation = self.orientation_var.get()
        success = self.game.place_ship(player, ship, pos, orientation)
        self.position_entry.delete(0, END)

        if not success and self.game.get_last_message():
            messagebox.showerror("Battleship", self.game.get_last_message())

    def show_remaining_ships(self):
        player = self.status_player.get()
        remaining = self.game.get_num_ships_remaining(player)
        self.status_label.config(text=f"{remaining} remaining")

    def build_grids(self, player):
        frame = self.frame_player1 if player == "first" else self.frame_player2

        for row in range(11):
            for col in range(11):
                if row == 0 and col == 0:
                    Label(frame, text=" ").grid(row=row, column=col)
                elif row == 0:
                    Label(frame, text=str(col)).grid(row=row, column=col)
                elif col == 0:
                    Label(frame, text=chr(64 + row)).grid(row=row, column=col)
                else:
                    btn = Button(frame, text=" ", width=2, height=1)
                    btn.grid(row=row, column=col)
                    self.player_buttons[player][(row - 1, col - 1)] = btn

                    if player == "second":
                        btn.config(command=lambda r=row-1, c=col-1: self.on_grid_click(r, c, shooter="first", target="second"))
                    elif player == "first":
                        btn.config(command=lambda r=row-1, c=col-1: self.on_grid_click(r, c, shooter="second", target="first"))

    def on_grid_click(self, x, y, shooter, target):
        coord_str = chr(65 + x) + str(y + 1)
        hit = self.game.fire_torpedo(shooter, coord_str)

        msg = self.game.get_last_message()
      
        if msg == "Not your turn.":
            return 
        btn = self.player_buttons[target].get((x, y))
        if btn:
            if hit:
                btn.config(text="X", bg="red")
            else:
                btn.config(text="O", bg="blue")


if __name__ == '__main__':
    root = Tk()
    app = BattleshipGUI(root)
    root.mainloop()
