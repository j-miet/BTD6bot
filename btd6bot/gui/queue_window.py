"""Contains QueueModeWindow class."""

from __future__ import annotations
import tkinter as tk

import gui.gui_paths as gui_paths
from utils import plan_data

class QueueModeWindow:
    """Allows adding and saving current queue list of plans.
    
    A separate Toplevel object is created so that other tkinter widgets can be placed inside it.

    Attributes:
        queue_optionwindow (tk.Toplevel): Toplevel object that creates a new window where other elements can be 
            inserted.
        myplans (tk.Listbox): Holds all user-selected plans.
        myplanslabel (tk.Label): Label displaying text above mymaps.
        delbutton (tk.Button): Button handling the removing of user-selected plans.
        allplans (tk.Label): Listbox of all existing plans.
        allplanslabel (tk.Label): Label displaying text above allmaps.
        up (tk.Button): Button for moving position of currently chosen plan one step up in mymaps.
        down (tk.Button): Button for moving position of currently chosen plan one step down in mymaps.
    """
    def __init__(self) -> None:
        """Initialize queue mode window."""
        self.queue_optionwindow = tk.Toplevel()
        self.queue_optionwindow.title("Queue map list")
        self.queue_optionwindow.geometry('550x400+100+550')
        self.queue_optionwindow.minsize(550,400)
        self.queue_optionwindow.maxsize(550,400)

        self.myplans = tk.Listbox(self.queue_optionwindow, width=40, height=20)
        self.myplans.grid(column=0, row=1, padx=11)
        self.myplanslabel = tk.Label(self.queue_optionwindow, text='Current queue')
        self.myplanslabel.grid(column=0, row=0)

        self.delbutton = tk.Button(self.queue_optionwindow, text='Remove (r)', command=self.remove_plan, width=10)
        self.delbutton.grid(column=0, row=2)
        self.queue_optionwindow.bind("r", lambda _: self.remove_plan())

        self.allplans = tk.Listbox(self.queue_optionwindow, width=40, height=20)
        self.allplans.grid(column=2, row=1, padx=11)
        self.allplanslabel = tk.Label(self.queue_optionwindow, text='All plans')
        self.allplanslabel.grid(column=2, row=0)

        self.addbutton = tk.Button(self.queue_optionwindow, text='Add (a)', command=self.add_plan, width=10)
        self.addbutton.grid(column=2, row=2)
        self.queue_optionwindow.bind("a", lambda _: self.add_plan())

        self.up = tk.Button(self.queue_optionwindow, text=u'\u2191' , width=1, height=5, command=self.move_up)
        self.up.grid(column=1, row=1, sticky='n')

        self.down = tk.Button(self.queue_optionwindow, text=u'\u2193' , width=1, height=5, command=self.move_down)
        self.down.grid(column=1, row=1, sticky='s')

        self.read_queue_list()
        self.read_allplans_list()

    def move_up(self) -> None:
        """Handles moving currently selected row up."""
        index = self.myplans.curselection() # type: ignore
        if index == () or index[0] == 0:
            return
        current_line = self.myplans.get(index[0])
        self.myplans.delete(index[0])
        self.myplans.insert(index[0]-1, current_line)
        
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed = file_read.readlines()
        listed.pop(index[0])
        listed.insert(index[0]-1, current_line+'\n')
        plan_data.list_format(listed)
        with open(gui_paths.QUEUE_LIST_PATH, 'w') as file_write:
            for line in listed:
                file_write.write(line)  

    def move_down(self) -> None:
        """Handles moving currently selected row down."""
        index = self.myplans.curselection() # type: ignore
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed = file_read.readlines()
        if index == () or index[0] == len(listed)-1:
            return
        current_line = self.myplans.get(index[0])
        self.myplans.delete(index[0])
        self.myplans.insert(index[0]+1, current_line)

        listed.pop(index[0])
        listed.insert(index[0]+1, current_line+'\n')
        plan_data.list_format(listed)
        with open(gui_paths.QUEUE_LIST_PATH, 'w') as file_write:
            for line in listed:
                file_write.write(line)

    def add_plan(self) -> None:
        """Add a new plan to current queue.
        
        Won't add a plan if it's already in queue.
        """
        index = self.allplans.curselection() # type: ignore
        if index == ():
            return
        selected_plan = self.allplans.get(index[0])
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed_plans = plan_data.list_format(file_read.readlines())
        if selected_plan in listed_plans:
            return
        self.myplans.insert(tk.END, selected_plan)
        with open(gui_paths.QUEUE_LIST_PATH, 'a') as file_append:
            file_append.write(self.allplans.get(index[0])+'\n')
        
    def remove_plan(self) -> None:
        """Remove a plan from current queue."""
        index = self.myplans.curselection() # type: ignore
        if index == ():
            return
        self.myplans.delete(index[0])    
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed = file_read.readlines()
        listed.pop(index[0])
        plan_data.list_format(listed)
        with open(gui_paths.QUEUE_LIST_PATH, 'w') as file_write:
            for line in listed:
                file_write.write(line)
            
    def read_queue_list(self) -> None:
        """Load an existing list of queued plans.
        
        Will also check whether all currently queued plans are found. If not, removes them automatically.
        """
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed_plans_raw = file_read.readlines()
            listed_plans = plan_data.list_format(listed_plans_raw)
        all_plans = plan_data.read_plans()
        if listed_plans != [] and set(listed_plans) not in set(all_plans):
            for plan in listed_plans:
                if plan not in all_plans:
                    try:
                        listed_plans.remove(plan)
                    except ValueError:
                        ...
            with open(gui_paths.QUEUE_LIST_PATH, 'w') as file_write:
                for line in listed_plans:
                    file_write.write(line+'\n')
        for i in range(0, len(listed_plans)):
            self.myplans.insert(i, listed_plans[i])

    def read_allplans_list(self) -> None:
        """Load a list of all existing plans."""
        all_plans = plan_data.read_plans()
        for i in range(0, len(all_plans)):
            self.allplans.insert(i, all_plans[i])

    def get_optionwindow(self) -> tk.Toplevel:
        """Get current option window.
        
        Returns:
            Current Toplevel window object of QueueModeWindow.
        """
        return self.queue_optionwindow