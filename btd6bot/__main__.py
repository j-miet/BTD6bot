"""Welcome to BTD6bot!"""

import pathlib
import sys
import tkinter as tk

import _no_gui
from gui.main_window import MainWindow
    
def main(argv: list[str]) -> None:
    """Main function.

    Args:
        argv (list[str]): Command line argument list. Only supported custom arg is '-nogui' which runs BTD6bot in 
            gui-free mode.
    """
    if len(argv) > 1 and argv[1] == '-nogui':
        _no_gui.run()
    else:
        root = tk.Tk()
        root.iconbitmap(pathlib.Path(__file__).parent/'Files'/"btd6bot.ico")
        MainWindow(root)
        root.mainloop()

if __name__ == '__main__':
    main(sys.argv)