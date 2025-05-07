from tkinter import Tk
from gui.main_window import BattleshipGUI


def main():
    root = Tk()
    app = BattleshipGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
