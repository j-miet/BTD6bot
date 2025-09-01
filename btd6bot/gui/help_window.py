"""Contains HelpWindow class."""

from __future__ import annotations
import tkinter as tk

import markdown # type: ignore
from tkinterweb import HtmlFrame # type: ignore

import gui.gui_paths as gui_paths

class HelpWindow:
    """Display help text window.

    A separate Toplevel object is created so that other tkinter widgets can be placed inside it.

    Attributes:
        helpwindow (tk.Toplevel): Toplevel object that creates a new window where other elements can be inserted.
        helpframe (tkinterweb.HtmlFrame): Frame for displaying html data, in particular readme markdown data converted 
            to html format.
    """
    def __init__(self) -> None:
        """Initialize help window.""" 
        self.helpwindow = tk.Toplevel()
        self.helpwindow.title("Help")
        self.helpwindow.iconbitmap(gui_paths.FILES_PATH/'btd6bot.ico')
        self.helpwindow.columnconfigure(0, weight=1)
        self.helpwindow.rowconfigure(0, weight=1)
        self.helpwindow.geometry("+50+50")

        self._update_imagepaths("docs", "file:/"+str(gui_paths.FILES_PATH).replace('\\', '/')+"/helpwindow/")
        self._update_markdown_to_html("file:/"+str(gui_paths.FILES_PATH).replace('\\', '/')+"/helpwindow/", "docs")

        self.helpframe = HtmlFrame(self.helpwindow, dark_theme_enabled=True)
        self.helpframe.load_file(str(gui_paths.FILES_PATH/'helpwindow'/'README.html'))
        self.helpframe.grid(column=0, row=0, sticky="nsew")

    def _update_imagepaths(self, old_path: str, new_path: str) -> None:
        with open(gui_paths.FILES_PATH/'helpwindow'/'README.md') as f:
            text = f.read()
        updated = text.replace(old_path, new_path)
        with open(gui_paths.FILES_PATH/'helpwindow'/'README.md', 'w') as newf:
            newf.write(updated)
        
    def _update_markdown_to_html(self, old_path: str, new_path: str) -> None:
        with open(gui_paths.FILES_PATH/'helpwindow'/'README.md') as f:
            text = f.read()
        html = markdown.markdown(text, extensions=['tables'])
        with open(gui_paths.FILES_PATH/'helpwindow'/'README.html', 'w') as outf:
            outf.write(html)
        updated = text.replace(old_path, new_path)
        with open(gui_paths.FILES_PATH/'helpwindow'/'README.md', 'w') as newf:
            newf.write(updated)

    def get_helpwindow(self) -> tk.Toplevel:
        """Get current help window.

        Returns:
            Current Toplevel window object of HelpWindow.
        """
        return self.helpwindow