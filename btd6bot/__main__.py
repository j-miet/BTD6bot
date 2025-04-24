"""Welcome to BTD6bot!

Gui is used by default, but if for some reason you'd like the command line version, use the 
run-ng.bat file located in the project root folder. Note that Gui-free version lacks most of the features, through.
"""

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