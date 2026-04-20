"""Welcome to BTD6bot!"""

import pathlib
import sys
import tkinter as tk

from _no_gui import NoGui
from gui.main_window import MainWindow


def main(argv: list[str]) -> None:
    """Main function.

    Args:
        argv (list[str]): Command line argument list. Only supported custom arg is '-nogui' which runs BTD6bot in
            gui-free mode.
    """
    if len(argv) > 1 and argv[1] == "-nogui":
        nogui = NoGui()
        nogui.run()
    else:
        root = tk.Tk()
        icon = tk.PhotoImage(file=pathlib.Path(__file__).parent / "Files" / "btd6bot.png")
        root.iconphoto(True, icon)
        MainWindow(root)
        root.mainloop()


if __name__ == "__main__":
    main(sys.argv)
