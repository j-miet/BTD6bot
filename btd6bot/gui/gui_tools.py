"""Thread termination (to close gui windows) and redirecting sys.stdout to MonitoringScreen Text panel.

Also includes get_osfont for getting properly adjusted fonts for each supported operating system.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import ctypes
from sys import platform
from tkinter import TclError

if TYPE_CHECKING:
    from threading import Thread
    from tkinter import Text

def terminate_thread(thread: Thread) -> None:
    """
    Terminates a python thread from another thread --- Use with caution!

    Original:
    https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread/15274929#15274929

    Args:
        thread: A threading.Thread instance.
    """
    if not thread.is_alive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc) # type: ignore[arg-type]
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def get_osfont() -> tuple[str, int]:
    """Font size for each operating system."""
    if platform == "win32":
        return ('Arial', 9)
    elif platform == "darwin":
        return ('Arial', 12)
    else: # after testing other OS such as linux, add them here too
        return ('Arial', 9)
    
os_font: tuple[str, int] = get_osfont()
"""Font for current operating system."""

class TextRedirector(object):
    """Class to redirect standard output into tkinter Text. Implements its own print method with write.

    If forced to shut down when MonitoringWindow is still open and not knowing how to handle buffered output, throws an 
    AttributeError: for this reason, a flush() prototype is implemented.

    Original:
    https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget/12352237#12352237

    Attributes:
        widget: A tkinter.Text object.
        tag: String tag for optional text formatting purposes.
    """
    def __init__(self, widget: Text, tag: str = "stdout"):
        """Initializes TextRedirector.

        Args:
            widget: Text object where text is redirected.
            tag: String tag for text formatting. Not currently used. Default value is "stdout".
        """
        self.widget = widget
        self.tag = tag

    def write(self, string : str) -> None:
        """print() implementation for Text widget.
        
        If user closes the monitoring window during bot running, and it happens so that widget existence status is 
        confirmed just before it closes, then print might get access no non-existent window (even if this time window 
        is incredibly brief) and throw tkinter.TclError. This error will be handled, even if user is very unlikely to
        notice anything as it gets printed to command line.
        """
        try:
            if self.widget.winfo_exists():
                self.widget.configure(state="normal")
                self.widget.insert("end", string, (self.tag))
                self.widget.configure(state="disabled")
                self.widget.see("end")
        except TclError:
            ...

    def flush(self) -> None:
        """Flush prototype for Text widget; only used through write() so don't call it on its own.
        
        After closing current monitoring window and redirecting stdout back to standard stream, current stream's 
        buffered output needs to flushed. This method's only purpose is to handle the possible error with flushing 
        after Text widget is dereferenced.
        """
        ...