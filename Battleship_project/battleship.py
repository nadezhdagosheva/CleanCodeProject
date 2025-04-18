import os
from tkinter import *
from ship_game_classes import ShipGame


class BattleshipGUI:
    
    def __init__(self, root):
    
        self.root = root
        self.root.geometry("750x550")
        self.root.title('Battleship')

        # Set window icon if the .ico file exists
        icon_path = os.path.abspath("battleship-icon.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.game = ShipGame()  # Main game logic instance

        # GUI control variables
        self.player_turn_var = StringVar(value='first')
        self.ship_choice_var = StringVar(value="carrier")
        self.orientation_var = StringVar(value="R")
        self.status_player = StringVar(value='first')

        self.position_entry = None
        self.ships_frame = None
        self.status_label = None

        # Store references to grid buttons for both players
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
        #Create controls to select ship type, orientation, and position.
        controls_frame = LabelFrame(self.root, text="Place Ship", padx=15, pady=15)
        controls_frame.grid(row=1, column=0, padx=30, pady=20)

        # Select player
        Radiobutton(controls_frame, text="Player1", variable=self.player_turn_var, value='first').grid(row=0, column=0)
        Radiobutton(controls_frame, text="Player2", variable=self.player_turn_var, value='second').grid(row=0, column=1)

        # Ship selection dropdown
        OptionMenu(controls_frame, self.ship_choice_var, "carrier", "battle-ship", "cruiser", "submarine", "destroyer").grid(row=1, column=0)

        # Position input
        self.position_entry = Entry(controls_frame, width=5)
        self.position_entry.grid(row=1, column=1)

        # Orientation selection
        Radiobutton(controls_frame, text="Row", variable=self.orientation_var, value='R').grid(row=1, column=2)
        Radiobutton(controls_frame, text="Col", variable=self.orientation_var, value='C').grid(row=1, column=3)

        # Submit button
        Button(controls_frame, text="Place the ship", command=self.place_ship).grid(row=2, column=3)

    def build_status_panel(self):
        #Create UI for showing remaining ships per player.
        self.ships_frame = LabelFrame(self.root, text="Ships Remaining", padx=15, pady=15)
        self.ships_frame.grid(row=1, column=1, padx=10, pady=10)

        # Player selector
        Radiobutton(self.ships_frame, text="Player1", variable=self.status_player, value='first').grid(row=0, column=0)
        Radiobutton(self.ships_frame, text="Player2", variable=self.status_player, value='second').grid(row=0, column=1)

        # Show button and label
        Button(self.ships_frame, text="Show ships", command=self.show_remaining_ships).grid(row=1, column=0)
        self.status_label = Label(self.ships_frame, text="")
        self.status_label.grid(row=1, column=1)

    def place_ship(self):
       
        player = self.player_turn_var.get()
        ship = self.ship_choice_var.get().strip()
        pos = self.position_entry.get()
        orientation = self.orientation_var.get()
        self.game.place_ship(player, ship, pos, orientation)
        self.position_entry.delete(0, END)

    def show_remaining_ships(self):
       
        player = self.status_player.get()
        remaining = self.game.get_num_ships_remaining(player)
        self.status_label.config(text=f"{remaining} remaining")

    def build_grids(self, player):
        
        frame = self.frame_player1 if player == "first" else self.frame_player2

        for row in range(11):
            for col in range(11):
                if row == 0 and col == 0:
                    Label(frame, text=" ").grid(row=row, column=col)  # Top-left empty label
                elif row == 0:
                    Label(frame, text=str(col)).grid(row=row, column=col)  # Column headers
                elif col == 0:
                    Label(frame, text=chr(64 + row)).grid(row=row, column=col)  # Row headers (A-J)
                else:
                    pos_str = chr(64 + row) + str(col)
                    btn = Button(
                        frame, text=" ", width=2, height=1,
                        command=lambda p=player, pos=pos_str: self.fire_torpedo(p, pos_str)
                    )
                    btn.grid(row=row, column=col)
                    self.player_buttons[player][(row - 1, col - 1)] = btn

    def fire_torpedo(self, player, pos):
        """Fire a torpedo at a position on the opponent's board and update UI."""
        opponent = "second" if player == "first" else "first"
        letter = pos[0].upper()
        x = self.game._letters_to_numbers.get(letter, -1)
        try:
            y = int(pos[1:]) - 1
        except ValueError:
            return

        if x not in range(10) or y not in range(10):
            return

        btn = self.player_buttons[opponent].get((x, y))
        hit_success = self.game.fire_torpedo(player, pos)

        if btn:
            if hit_success:
                btn.config(text="X", bg="red")
            else:
                btn.config(text="O", bg="blue")


# Start the GUI application
if __name__ == '__main__':
    root = Tk()
    app = BattleshipGUI(root)
    root.mainloop()
