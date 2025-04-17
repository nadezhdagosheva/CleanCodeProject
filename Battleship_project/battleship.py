from ship_game_classes import ShipGame
from tkinter import *

s = ShipGame()

root = Tk()
root.geometry("750x550")
root.title('Battleship')
root.iconbitmap('battleship-icon.ico')

# frame for game board grids
frame1 = LabelFrame(root, text="Player1", padx=10, pady=10)
frame1.grid(row=0, column=0, padx=10, pady=10)
frame2 = LabelFrame(root, text="Player2", padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

# frame for data input
frame3 = LabelFrame(root, text="Place Ship", padx=15, pady=15)
frame3.grid(row=1, column=0, padx=30, pady=20)

# frame for ships remaining
frame4 = LabelFrame(root, text="Ships Remaining", padx=15, pady=15)
frame4.grid(row=1, column=1, padx=10, pady=10)

# which player is making move
player = StringVar()
player.set('first')
Radiobutton(frame3, text="Player1", variable=player, value='first').grid(row=0, column=0)
Radiobutton(frame3, text="Player2", variable=player, value='second').grid(row=0, column=1)

# drop menu for ships
clicked = StringVar()
clicked.set("carrier        ")

options = OptionMenu(frame3, clicked, "carrier        ", "battle-ship", "cruiser       ", "submarine", "destroyer   ")
options.grid(row=1, column=0)

# choose position
pos = Entry(frame3, width=5)
pos.grid(row=1, column=1)

# choose orientation
orientation = StringVar()
orientation.set("R")
Radiobutton(frame3, text="Row", variable=orientation, value='R').grid(row=1, column=2)
Radiobutton(frame3, text="Col", variable=orientation, value='C').grid(row=1, column=3)


def submit_click(player, ship, pos, orientation):
    s.place_ship(player, ship, pos.get(), orientation)
    pos.delete(0, END)


emptyLabel = Label(frame3, text=" ")
emptyLabel.grid(row=2, column=0, columnspan=2)
# button for finalizing placing ship
submit = Button(frame3, text="Place the ship",
                command=lambda: submit_click(player.get(), clicked.get().strip(), pos, orientation.get()))
submit.grid(row=2, column=3)


def show_num_ships_remaining(player):
    num_ships = s.get_num_ships_remaining(player)
    message_label = Label(frame4, text="{} remaining".format(num_ships))
    message_label.grid(row=1, column=1)


# which players ships to show
player_show = StringVar()
player_show.set('first')
Radiobutton(frame4, text="Player1", variable=player_show, value='first').grid(row=0, column=0)
Radiobutton(frame4, text="Player2", variable=player_show, value='second').grid(row=0, column=1)

# button for showing player's remaining ships
show = Button(frame4, text="Show ships", command=lambda: show_num_ships_remaining(player_show.get()))
show.grid(row=1, column=0)

# game board buttons

# Player1 board
# grid coordinates - alphabet
a_label = Label(frame1, text="A")
a_label.grid(row=1, column=0)
b_label = Label(frame1, text="B")
b_label.grid(row=2, column=0)
c_label = Label(frame1, text="C")
c_label.grid(row=3, column=0)
d_label = Label(frame1, text="D")
d_label.grid(row=4, column=0)
e_label = Label(frame1, text="E")
e_label.grid(row=5, column=0)
f_label = Label(frame1, text="F")
f_label.grid(row=6, column=0)
g_label = Label(frame1, text="G")
g_label.grid(row=7, column=0)
h_label = Label(frame1, text="H")
h_label.grid(row=8, column=0)
i_label = Label(frame1, text="I")
i_label.grid(row=9, column=0)
j_label = Label(frame1, text="J")
j_label.grid(row=10, column=0)

# grid coordinates - digits
blank_label2 = Label(frame1, text=" ")
blank_label2.grid(row=0, column=0)
label_1 = Label(frame1, text="1")
label_1.grid(row=0, column=1)
label_2 = Label(frame1, text="2")
label_2.grid(row=0, column=2)
label_3 = Label(frame1, text="3")
label_3.grid(row=0, column=3)
label_4 = Label(frame1, text="4")
label_4.grid(row=0, column=4)
label_5 = Label(frame1, text="5")
label_5.grid(row=0, column=5)
label_6 = Label(frame1, text="6")
label_6.grid(row=0, column=6)
label_7 = Label(frame1, text="7")
label_7.grid(row=0, column=7)
label_8 = Label(frame1, text="8")
label_8.grid(row=0, column=8)
label_9 = Label(frame1, text="9")
label_9.grid(row=0, column=9)
label_10 = Label(frame1, text="10")
label_10.grid(row=0, column=10)

# row 1
p1_A1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A1", p1_A1))
p1_A1.grid(row=1, column=1)
p1_A2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A2", p1_A2))
p1_A2.grid(row=1, column=2)
p1_A3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A3", p1_A3))
p1_A3.grid(row=1, column=3)
p1_A4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A4", p1_A4))
p1_A4.grid(row=1, column=4)
p1_A5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A5", p1_A5))
p1_A5.grid(row=1, column=5)
p1_A6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A6", p1_A6))
p1_A6.grid(row=1, column=6)
p1_A7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A7", p1_A7))
p1_A7.grid(row=1, column=7)
p1_A8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A8", p1_A8))
p1_A8.grid(row=1, column=8)
p1_A9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A9", p1_A9))
p1_A9.grid(row=1, column=9)
p1_A10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "A10", p1_A10))
p1_A10.grid(row=1, column=10)
# row 2
p1_B1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B1", p1_B1))
p1_B1.grid(row=2, column=1)
p1_B2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B2", p1_B2))
p1_B2.grid(row=2, column=2)
p1_B3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B3", p1_B3))
p1_B3.grid(row=2, column=3)
p1_B4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B4", p1_B4))
p1_B4.grid(row=2, column=4)
p1_B5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B5", p1_B5))
p1_B5.grid(row=2, column=5)
p1_B6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B6", p1_B6))
p1_B6.grid(row=2, column=6)
p1_B7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B7", p1_B7))
p1_B7.grid(row=2, column=7)
p1_B8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B8", p1_B8))
p1_B8.grid(row=2, column=8)
p1_B9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B9", p1_B9))
p1_B9.grid(row=2, column=9)
p1_B10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "B10", p1_B10))
p1_B10.grid(row=2, column=10)

# row 3
p1_C1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C1", p1_C1))
p1_C1.grid(row=3, column=1)
p1_C2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C2", p1_C2))
p1_C2.grid(row=3, column=2)
p1_C3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C3", p1_C3))
p1_C3.grid(row=3, column=3)
p1_C4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C4", p1_C4))
p1_C4.grid(row=3, column=4)
p1_C5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C5", p1_C5))
p1_C5.grid(row=3, column=5)
p1_C6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C6", p1_C6))
p1_C6.grid(row=3, column=6)
p1_C7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C7", p1_C7))
p1_C7.grid(row=3, column=7)
p1_C8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C8", p1_C8))
p1_C8.grid(row=3, column=8)
p1_C9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C9", p1_C9))
p1_C9.grid(row=3, column=9)
p1_C10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "C10", p1_C10))
p1_C10.grid(row=3, column=10)
# row 4
p1_D1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D1", p1_D1))
p1_D1.grid(row=4, column=1)
p1_D2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D2", p1_D2))
p1_D2.grid(row=4, column=2)
p1_D3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D3", p1_D3))
p1_D3.grid(row=4, column=3)
p1_D4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D4", p1_D4))
p1_D4.grid(row=4, column=4)
p1_D5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D5", p1_D5))
p1_D5.grid(row=4, column=5)
p1_D6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D6", p1_D6))
p1_D6.grid(row=4, column=6)
p1_D7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D7", p1_D7))
p1_D7.grid(row=4, column=7)
p1_D8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D8", p1_D8))
p1_D8.grid(row=4, column=8)
p1_D9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D9", p1_D9))
p1_D9.grid(row=4, column=9)
p1_D10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "D10", p1_D10))
p1_D10.grid(row=4, column=10)
# row 5
p1_E1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E1", p1_E1))
p1_E1.grid(row=5, column=1)
p1_E2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E2", p1_E2))
p1_E2.grid(row=5, column=2)
p1_E3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E3", p1_E3))
p1_E3.grid(row=5, column=3)
p1_E4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E4", p1_E4))
p1_E4.grid(row=5, column=4)
p1_E5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E5", p1_E5))
p1_E5.grid(row=5, column=5)
p1_E6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E6", p1_E6))
p1_E6.grid(row=5, column=6)
p1_E7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E7", p1_E7))
p1_E7.grid(row=5, column=7)
p1_E8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E8", p1_E8))
p1_E8.grid(row=5, column=8)
p1_E9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E9", p1_E9))
p1_E9.grid(row=5, column=9)
p1_E10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "E10", p1_E10))
p1_E10.grid(row=5, column=10)
# row 6
p1_F1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F1", p1_F1))
p1_F1.grid(row=6, column=1)
p1_F2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F2", p1_F2))
p1_F2.grid(row=6, column=2)
p1_F3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F3", p1_F3))
p1_F3.grid(row=6, column=3)
p1_F4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F4", p1_F4))
p1_F4.grid(row=6, column=4)
p1_F5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F5", p1_F5))
p1_F5.grid(row=6, column=5)
p1_F6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F6", p1_F6))
p1_F6.grid(row=6, column=6)
p1_F7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F7", p1_F7))
p1_F7.grid(row=6, column=7)
p1_F8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F8", p1_F8))
p1_F8.grid(row=6, column=8)
p1_F9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F9", p1_F9))
p1_F9.grid(row=6, column=9)
p1_F10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "F10", p1_F10))
p1_F10.grid(row=6, column=10)
# row 7
p1_G1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G1", p1_G1))
p1_G1.grid(row=7, column=1)
p1_G2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G2", p1_G2))
p1_G2.grid(row=7, column=2)
p1_G3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G3", p1_G3))
p1_G3.grid(row=7, column=3)
p1_G4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G4", p1_G4))
p1_G4.grid(row=7, column=4)
p1_G5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G5", p1_G5))
p1_G5.grid(row=7, column=5)
p1_G6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G6", p1_G6))
p1_G6.grid(row=7, column=6)
p1_G7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G7", p1_G7))
p1_G7.grid(row=7, column=7)
p1_G8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G8", p1_G8))
p1_G8.grid(row=7, column=8)
p1_G9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G9", p1_G9))
p1_G9.grid(row=7, column=9)
p1_G10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "G10", p1_G10))
p1_G10.grid(row=7, column=10)
# row 8
p1_H1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H1", p1_H1))
p1_H1.grid(row=8, column=1)
p1_H2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H2", p1_H2))
p1_H2.grid(row=8, column=2)
p1_H3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H3", p1_H3))
p1_H3.grid(row=8, column=3)
p1_H4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H4", p1_H4))
p1_H4.grid(row=8, column=4)
p1_H5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H5", p1_H5))
p1_H5.grid(row=8, column=5)
p1_H6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H6", p1_H6))
p1_H6.grid(row=8, column=6)
p1_H7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H7", p1_H7))
p1_H7.grid(row=8, column=7)
p1_H8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H8", p1_H8))
p1_H8.grid(row=8, column=8)
p1_H9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H9", p1_H9))
p1_H9.grid(row=8, column=9)
p1_H0 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H10", p1_H0))
p1_H0.grid(row=8, column=10)
# row 9
p1_I1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I1", p1_I1))
p1_I1.grid(row=9, column=1)
p1_I2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I2", p1_I2))
p1_I2.grid(row=9, column=2)
p1_I3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I3", p1_I3))
p1_I3.grid(row=9, column=3)
p1_I4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I4", p1_I4))
p1_I4.grid(row=9, column=4)
p1_I5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I5", p1_I5))
p1_I5.grid(row=9, column=5)
p1_I6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I6", p1_I6))
p1_I6.grid(row=9, column=6)
p1_I7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I7", p1_I7))
p1_I7.grid(row=9, column=7)
p1_I8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I8", p1_I8))
p1_I8.grid(row=9, column=8)
p1_I9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I9", p1_I9))
p1_I9.grid(row=9, column=9)
p1_I10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "I10", p1_I10))
p1_I10.grid(row=9, column=10)
# row 10
p1_J1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J1", p1_J1))
p1_J1.grid(row=10, column=1)
p1_J2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J2", p1_J2))
p1_J2.grid(row=10, column=2)
p1_J3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J3", p1_J3))
p1_J3.grid(row=10, column=3)
p1_J4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J4", p1_J4))
p1_J4.grid(row=10, column=4)
p1_J5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J5", p1_J5))
p1_J5.grid(row=10, column=5)
p1_J6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J6", p1_J6))
p1_J6.grid(row=10, column=6)
p1_J7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J7", p1_J7))
p1_J7.grid(row=10, column=7)
p1_J8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J8", p1_J8))
p1_J8.grid(row=10, column=8)
p1_J9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J9", p1_J9))
p1_J9.grid(row=10, column=9)
p1_J0 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J10", p1_J0))
p1_J0.grid(row=10, column=10)

# Player2 board
# grid coordinates - alphabet
a_label = Label(frame2, text="A")
a_label.grid(row=1, column=0)
b_label = Label(frame2, text="B")
b_label.grid(row=2, column=0)
c_label = Label(frame2, text="C")
c_label.grid(row=3, column=0)
d_label = Label(frame2, text="D")
d_label.grid(row=4, column=0)
e_label = Label(frame2, text="E")
e_label.grid(row=5, column=0)
f_label = Label(frame2, text="F")
f_label.grid(row=6, column=0)
g_label = Label(frame2, text="G")
g_label.grid(row=7, column=0)
h_label = Label(frame2, text="H")
h_label.grid(row=8, column=0)
i_label = Label(frame2, text="I")
i_label.grid(row=9, column=0)
j_label = Label(frame2, text="J")
j_label.grid(row=10, column=0)

# grid coordinates - digits
blank_label3 = Label(frame2, text=" ")
blank_label3.grid(row=0, column=0)
label_1 = Label(frame2, text="1")
label_1.grid(row=0, column=1)
label_2 = Label(frame2, text="2")
label_2.grid(row=0, column=2)
label_3 = Label(frame2, text="3")
label_3.grid(row=0, column=3)
label_4 = Label(frame2, text="4")
label_4.grid(row=0, column=4)
label_5 = Label(frame2, text="5")
label_5.grid(row=0, column=5)
label_6 = Label(frame2, text="6")
label_6.grid(row=0, column=6)
label_7 = Label(frame2, text="7")
label_7.grid(row=0, column=7)
label_8 = Label(frame2, text="8")
label_8.grid(row=0, column=8)
label_9 = Label(frame2, text="9")
label_9.grid(row=0, column=9)
label_10 = Label(frame2, text="10")
label_10.grid(row=0, column=10)

# row 1
p2_A1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A1", p2_A1))
p2_A1.grid(row=1, column=1)
p2_A2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A2", p2_A2))
p2_A2.grid(row=1, column=2)
p2_A3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A3", p2_A3))
p2_A3.grid(row=1, column=3)
p2_A4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A4", p2_A4))
p2_A4.grid(row=1, column=4)
p2_A5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A5", p2_A5))
p2_A5.grid(row=1, column=5)
p2_A6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A6", p2_A6))
p2_A6.grid(row=1, column=6)
p2_A7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A7", p2_A7))
p2_A7.grid(row=1, column=7)
p2_A8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A8", p2_A8))
p2_A8.grid(row=1, column=8)
p2_A9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "A9", p2_A9))
p2_A9.grid(row=1, column=9)
p2_A10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "A10", p2_A10))
p2_A10.grid(row=1, column=10)
# row 2
p2_B1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B1", p2_B1))
p2_B1.grid(row=2, column=1)
p2_B2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B2", p2_B2))
p2_B2.grid(row=2, column=2)
p2_B3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B3", p2_B3))
p2_B3.grid(row=2, column=3)
p2_B4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B4", p2_B4))
p2_B4.grid(row=2, column=4)
p2_B5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B5", p2_B5))
p2_B5.grid(row=2, column=5)
p2_B6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B6", p2_B6))
p2_B6.grid(row=2, column=6)
p2_B7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B7", p2_B7))
p2_B7.grid(row=2, column=7)
p2_B8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B8", p2_B8))
p2_B8.grid(row=2, column=8)
p2_B9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "B9", p2_B9))
p2_B9.grid(row=2, column=9)
p2_B10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "B10", p2_B10))
p2_B10.grid(row=2, column=10)
# row 3
p2_C1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C1", p2_C1))
p2_C1.grid(row=3, column=1)
p2_C2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C2", p2_C2))
p2_C2.grid(row=3, column=2)
p2_C3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C3", p2_C3))
p2_C3.grid(row=3, column=3)
p2_C4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C4", p2_C4))
p2_C4.grid(row=3, column=4)
p2_C5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C5", p2_C5))
p2_C5.grid(row=3, column=5)
p2_C6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C6", p2_C6))
p2_C6.grid(row=3, column=6)
p2_C7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C7", p2_C7))
p2_C7.grid(row=3, column=7)
p2_C8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C8", p2_C8))
p2_C8.grid(row=3, column=8)
p2_C9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "C9", p2_C9))
p2_C9.grid(row=3, column=9)
p2_C10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "C10", p2_C10))
p2_C10.grid(row=3, column=10)
# row 4
p2_D1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D1", p2_D1))
p2_D1.grid(row=4, column=1)
p2_D2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D2", p2_D2))
p2_D2.grid(row=4, column=2)
p2_D3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D3", p2_D3))
p2_D3.grid(row=4, column=3)
p2_D4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D4", p2_D4))
p2_D4.grid(row=4, column=4)
p2_D5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D5", p2_D5))
p2_D5.grid(row=4, column=5)
p2_D6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D6", p2_D6))
p2_D6.grid(row=4, column=6)
p2_D7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D7", p2_D7))
p2_D7.grid(row=4, column=7)
p2_D8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D8", p2_D8))
p2_D8.grid(row=4, column=8)
p2_D9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "D9", p2_D9))
p2_D9.grid(row=4, column=9)
p2_D10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "D10", p2_D10))
p2_D10.grid(row=4, column=10)
# row 5
p2_E1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E1", p2_E1))
p2_E1.grid(row=5, column=1)
p2_E2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E2", p2_E2))
p2_E2.grid(row=5, column=2)
p2_E3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E3", p2_E3))
p2_E3.grid(row=5, column=3)
p2_E4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E4", p2_E4))
p2_E4.grid(row=5, column=4)
p2_E5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E5", p2_E5))
p2_E5.grid(row=5, column=5)
p2_E6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E6", p2_E6))
p2_E6.grid(row=5, column=6)
p2_E7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E7", p2_E7))
p2_E7.grid(row=5, column=7)
p2_E8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E8", p2_E8))
p2_E8.grid(row=5, column=8)
p2_E9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "E9", p2_E9))
p2_E9.grid(row=5, column=9)
p2_E10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "E10", p2_E10))
p2_E10.grid(row=5, column=10)
# row 6
p2_F1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F1", p2_F1))
p2_F1.grid(row=6, column=1)
p2_F2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F2", p2_F2))
p2_F2.grid(row=6, column=2)
p2_F3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F3", p2_F3))
p2_F3.grid(row=6, column=3)
p2_F4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F4", p2_F4))
p2_F4.grid(row=6, column=4)
p2_F5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F5", p2_F5))
p2_F5.grid(row=6, column=5)
p2_F6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F6", p2_F6))
p2_F6.grid(row=6, column=6)
p2_F7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F7", p2_F7))
p2_F7.grid(row=6, column=7)
p2_F8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F8", p2_F8))
p2_F8.grid(row=6, column=8)
p2_F9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "F9", p2_F9))
p2_F9.grid(row=6, column=9)
p2_F10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "F10", p2_F10))
p2_F10.grid(row=6, column=10)
# row 7
p2_G1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G1", p2_G1))
p2_G1.grid(row=7, column=1)
p2_G2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G2", p2_G2))
p2_G2.grid(row=7, column=2)
p2_G3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G3", p2_G3))
p2_G3.grid(row=7, column=3)
p2_G4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G4", p2_G4))
p2_G4.grid(row=7, column=4)
p2_G5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G5", p2_G5))
p2_G5.grid(row=7, column=5)
p2_G6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G6", p2_G6))
p2_G6.grid(row=7, column=6)
p2_G7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G7", p2_G7))
p2_G7.grid(row=7, column=7)
p2_G8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G8", p2_G8))
p2_G8.grid(row=7, column=8)
p2_G9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "G9", p2_G9))
p2_G9.grid(row=7, column=9)
p2_G10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "G10", p2_G10))
p2_G10.grid(row=7, column=10)
# row 8
p2_H1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H1", p2_H1))
p2_H1.grid(row=8, column=1)
p2_H2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H2", p2_H2))
p2_H2.grid(row=8, column=2)
p2_H3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H3", p2_H3))
p2_H3.grid(row=8, column=3)
p2_H4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H4", p2_H4))
p2_H4.grid(row=8, column=4)
p2_H5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H5", p2_H5))
p2_H5.grid(row=8, column=5)
p2_H6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H6", p2_H6))
p2_H6.grid(row=8, column=6)
p2_H7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H7", p2_H7))
p2_H7.grid(row=8, column=7)
p2_H8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H8", p2_H8))
p2_H8.grid(row=8, column=8)
p2_H9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H9", p2_H9))
p2_H9.grid(row=8, column=9)
p2_H0 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "H10", p2_H0))
p2_H0.grid(row=8, column=10)
# row 9
p2_I1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I1", p2_I1))
p2_I1.grid(row=9, column=1)
p2_I2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I2", p2_I2))
p2_I2.grid(row=9, column=2)
p2_I3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I3", p2_I3))
p2_I3.grid(row=9, column=3)
p2_I4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I4", p2_I4))
p2_I4.grid(row=9, column=4)
p2_I5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I5", p2_I5))
p2_I5.grid(row=9, column=5)
p2_I6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I6", p2_I6))
p2_I6.grid(row=9, column=6)
p2_I7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I7", p2_I7))
p2_I7.grid(row=9, column=7)
p2_I8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I8", p2_I8))
p2_I8.grid(row=9, column=8)
p2_I9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "I9", p2_I9))
p2_I9.grid(row=9, column=9)
p2_I10 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("second", "I10", p2_I10))
p2_I10.grid(row=9, column=10)
# row 10
p2_J1 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J1", p2_J1))
p2_J1.grid(row=10, column=1)
p2_J2 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J2", p2_J2))
p2_J2.grid(row=10, column=2)
p2_J3 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J3", p2_J3))
p2_J3.grid(row=10, column=3)
p2_J4 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J4", p2_J4))
p2_J4.grid(row=10, column=4)
p2_J5 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J5", p2_J5))
p2_J5.grid(row=10, column=5)
p2_J6 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J6", p2_J6))
p2_J6.grid(row=10, column=6)
p2_J7 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J7", p2_J7))
p2_J7.grid(row=10, column=7)
p2_J8 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J8", p2_J8))
p2_J8.grid(row=10, column=8)
p2_J9 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J9", p2_J9))
p2_J9.grid(row=10, column=9)
p2_J0 = Button(frame2, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("second", "J10", p2_J0))
p2_J0.grid(row=10, column=10)

root.mainloop()