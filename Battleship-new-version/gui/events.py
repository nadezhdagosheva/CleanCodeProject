from tkinter import messagebox

def place_ship(app):
    player = app.player_turn_var.get()
    ship = app.ship_choice_var.get().strip()
    pos = app.position_entry.get()
    orientation = app.orientation_var.get()
    success = app.game.place_ship(player, ship, pos, orientation)
    app.position_entry.delete(0, 'end')

    if not success and app.game.get_last_message():
        messagebox.showerror("Battleship", app.game.get_last_message())

def show_remaining_ships(app):
    player = app.status_player.get()
    remaining = app.game.get_num_ships_remaining(player)
    app.status_label.config(text=f"{remaining} remaining")

def handle_grid_click(app, x, y, shooter, target):
    coord_str = chr(65 + x) + str(y + 1)
    hit = app.game.fire_torpedo(shooter, coord_str)

    msg = app.game.get_last_message()
    if msg:
        msg = msg.replace("First", "Player 1").replace("Second", "Player 2")
        messagebox.showinfo("Battleship", msg)

    if msg in ["Not your turn.", "Game already finished."]:
        return

    btn = app.player_buttons[target].get((x, y))
    if btn:
        if hit:
            btn.config(text="X", bg="red")
        else:
            btn.config(text="O", bg="blue")
