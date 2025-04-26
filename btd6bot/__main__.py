"""Welcome to BTD6bot!"""

import sys
import tkinter as tk

import _no_gui
from gui.main_window import MainWindow
    
def main() -> None:
    """Creates a root window for GUI and passes it to MainWindow constructor.

    In order to make GUI objects appear onscreen and get updated constantly, root.mainloop is called.
    """
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-nogui':
        _no_gui.run()
    else:
        main()