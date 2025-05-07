from tkinter import *
from gui.events import place_ship, show_remaining_ships

def build_board_frames(app):
    app.frame_player1 = LabelFrame(app.root, text="Player1", padx=10, pady=10)
    app.frame_player1.grid(row=0, column=0, padx=10, pady=10)

    app.frame_player2 = LabelFrame(app.root, text="Player2", padx=10, pady=10)
    app.frame_player2.grid(row=0, column=1, padx=10, pady=10)

def build_ship_placement_controls(app):
    controls_frame = LabelFrame(app.root, text="Place Ship", padx=15, pady=15)
    controls_frame.grid(row=1, column=0, padx=30, pady=20)

    Radiobutton(controls_frame, text="Player1", variable=app.player_turn_var, value='first').grid(row=0, column=0)
    Radiobutton(controls_frame, text="Player2", variable=app.player_turn_var, value='second').grid(row=0, column=1)

    OptionMenu(controls_frame, app.ship_choice_var, "carrier", "battle-ship", "cruiser", "submarine", "destroyer").grid(row=1, column=0)

    app.position_entry = Entry(controls_frame, width=5)
    app.position_entry.grid(row=1, column=1)

    Radiobutton(controls_frame, text="Row", variable=app.orientation_var, value='R').grid(row=1, column=2)
    Radiobutton(controls_frame, text="Col", variable=app.orientation_var, value='C').grid(row=1, column=3)

    Button(controls_frame, text="Place the ship", command=lambda: place_ship(app)).grid(row=2, column=3)

def build_status_panel(app):
    app.ships_frame = LabelFrame(app.root, text="Ships Remaining", padx=15, pady=15)
    app.ships_frame.grid(row=1, column=1, padx=10, pady=10)

    Radiobutton(app.ships_frame, text="Player1", variable=app.status_player, value='first').grid(row=0, column=0)
    Radiobutton(app.ships_frame, text="Player2", variable=app.status_player, value='second').grid(row=0, column=1)

    Button(app.ships_frame, text="Show ships", command=lambda: show_remaining_ships(app)).grid(row=1, column=0)
    app.status_label = Label(app.ships_frame, text="")
    app.status_label.grid(row=1, column=1)

def build_grids(app, player):
    frame = app.frame_player1 if player == "first" else app.frame_player2

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
                app.player_buttons[player][(row - 1, col - 1)] = btn
                btn.config(command=lambda r=row-1, c=col-1: app.on_grid_click(r, c, shooter="second" if player == "first" else "first", target=player))
