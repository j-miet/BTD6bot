"""Contains HelpWindow class."""

from __future__ import annotations
import tkinter as tk

import gui.gui_paths as gui_paths

class HelpWindow:
    """Display help text window.

    A separate Toplevel object is created so that other tkinter widgets can be placed inside it.

    Compared to other window classs, its implementation is far simpler as it only displays text.

    Attributes:
        helpwindow (tk.Toplevel): Toplevel object that creates a new window where other elements can be inserted.
        helptextbox (tk.Text): Scrollbar that displays text and allows scrolling text up or down.
    """
    def __init__(self) -> None:
        """Initialize help window.""" 
        self.helpwindow = tk.Toplevel()
        self.helpwindow.title("Help")
        self.helpwindow.columnconfigure(0, weight=1)
        self.helpwindow.rowconfigure(0, weight=1)
        self.helpwindow.geometry("+50+50")

        self.helptextbox = tk.Text(self.helpwindow, state='normal')
        self.helptextbox.grid(column=0, row=0, sticky="nsew")
        self.write_helpboxtext()

        helpscroll = tk.Scrollbar(self.helpwindow, orient='vertical')
        helpscroll.grid(column=1, row=0, sticky="ns")
        self.helptextbox.configure(yscrollcommand=helpscroll.set)
        helpscroll.configure(command=self.helptextbox.yview)

    def write_helpboxtext(self) -> None:
        """Reads help/readme text from a file and insert it onto a Text object."""
        with open(gui_paths.HELP_PATH) as file_read:
            readme_text = file_read.readlines()
        for line in readme_text:
            self.helptextbox.insert('end', line)
        self.helptextbox['state'] = 'disabled'

    def get_helpwindow(self) -> tk.Toplevel:
        """Get current help window.

        Returns:
            Current Toplevel window object of HelpWindow.
        """
        return self.helpwindow