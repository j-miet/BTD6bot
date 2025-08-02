"""Contains QueueModeWindow class."""

from __future__ import annotations
import json

import tkinter as tk
from tkinter import ttk

import gui.gui_paths as gui_paths
from gui.gui_tools import os_font
from utils import plan_data

class QueueModeWindow:
    """Allows adding and saving current queue list of plans.
    
    A separate Toplevel object is created so that other tkinter widgets can be placed inside it.

    Attributes:
        queue_optionwindow (tk.Toplevel): Toplevel object that creates a new window where other elements can be 
            inserted.
        current_plan (str): Plan name string.
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
        self.queue_optionwindow.iconbitmap(gui_paths.FILES_PATH/'btd6bot.ico')
        self.queue_optionwindow.geometry('930x400+100+550')
        self.queue_optionwindow.minsize(930,400)
        self.queue_optionwindow.maxsize(930,400)

        currentplans_scroll = ttk.Scrollbar(self.queue_optionwindow, 
                                            orient='vertical')
        currentplans_scroll.grid(column=1, row=1, sticky="nsw")
        self.current_plan = ''
        self.myplanslabel = tk.Label(self.queue_optionwindow, 
                                     text='Current queue', 
                                     font=os_font)
        self.myplanslabel.grid(column=0, row=0)
        self.myplans = tk.Listbox(self.queue_optionwindow,
                                  width=36, 
                                  height=20, 
                                  yscrollcommand=currentplans_scroll.set, 
                                  font=os_font)
        self.myplans.grid(column=0, row=1, padx=(11, 0))
        self.myplans.bind("<<ListboxSelect>>", lambda _: self.update_planinfo())

        self.delbutton = tk.Button(self.queue_optionwindow, 
                                   text='Remove (r)', 
                                   command=self.remove_plan, 
                                   width=10, 
                                   font=os_font)
        self.delbutton.grid(column=0, row=2, sticky="w", padx=(11,0))
        self.queue_optionwindow.bind("r", lambda _: self.remove_plan())

        self.delall_button = tk.Button(self.queue_optionwindow, 
                                       text='Remove all', 
                                       command=self.remove_allcurrentplans, 
                                       width=10, 
                                       font=os_font)
        self.delall_button.grid(column=0, row=2, sticky="e", padx=(11,0))

        self.up = tk.Button(self.queue_optionwindow, 
                            text=u'\u2191', 
                            width=1, 
                            height=5, 
                            command=self.move_up,
                            font=os_font)
        self.up.grid(column=2, row=1, sticky='n')
        self.down = tk.Button(self.queue_optionwindow, 
                              text=u'\u2193', 
                              width=1, 
                              height=5, 
                              command=self.move_down,
                              font=os_font)
        self.down.grid(column=2, row=1, sticky='s')
    
        allplans_scroll = ttk.Scrollbar(self.queue_optionwindow, 
                                        orient='vertical')
        allplans_scroll.grid(column=4, row=1, sticky="nsw", padx=(0, 11))
        self.allplanslabel = tk.Label(self.queue_optionwindow, 
                                      text='All plans', 
                                      font=os_font)
        self.allplanslabel.grid(column=3, row=0)
        self.allplans = tk.Listbox(self.queue_optionwindow, 
                                   width=36, 
                                   height=20, 
                                   yscrollcommand=allplans_scroll.set,
                                   font=os_font)
        self.allplans.grid(column=3, row=1, padx=(11, 0))
        self.allplans.bind("<<ListboxSelect>>", lambda _: self.update_planinfo())

        self.addbutton = tk.Button(self.queue_optionwindow, 
                                   text='Add (a)', 
                                   command=self.add_plan, 
                                   width=10, 
                                   font=os_font)
        self.addbutton.grid(column=3, row=2, sticky="w", padx=(11,0))
        self.queue_optionwindow.bind("a", lambda _: self.add_plan())

        info_window_scroll = ttk.Scrollbar(self.queue_optionwindow, 
                                           orient='vertical')
        info_window_scroll.grid(column=6, row=1, sticky="nsw")
        self.infolabel = tk.Label(self.queue_optionwindow, 
                                  text='Plan info', 
                                  font=os_font)
        self.infolabel.grid(column=5, row=0)
        self.info_window = tk.Text(self.queue_optionwindow, 
                                   height=18, 
                                   width=40, 
                                   yscrollcommand=info_window_scroll.set, 
                                   font=os_font, 
                                   wrap=tk.WORD, 
                                   relief='sunken', 
                                   padx=11)
        self.info_window.grid(column=5, row=1, sticky='ns')
        self.info_window['state'] = 'disabled'
        info_window_scroll.configure(command=self.info_window.yview)

        self.all_searchbartext = tk.StringVar(value="")
        self.all_searchbartext.trace_add("write", lambda r, w, u: self._callback_all())
        self.all_searchbar = tk.Entry(self.queue_optionwindow, 
                                      textvariable=self.all_searchbartext, 
                                      font=os_font)
        self.all_searchbar.grid(column=3, row=2, sticky="e")
        self.all_searchbar.insert(0, "search plans...")
        self.all_searchbar.bind('<FocusIn>', lambda _: self._clear_entry())
        self.all_searchbar.config(fg='grey')

        self.read_queue_list()
        self.read_allplans_list()

    def _clear_entry(self) -> None:
        if self.all_searchbar.get() == 'search plans...':
            self.all_searchbar.delete(0, "end")
            self.all_searchbar.config(fg='black')

    def _callback_all(self) -> None:
        searchtext = self.all_searchbartext.get()
        all_plans = plan_data.read_plans()
        matching_plans: list[str] = []
        for plan_name in all_plans:
            if searchtext in plan_name:
                matching_plans.append(plan_name)
        self.allplans.delete(0, "end")
        for i in range(0, len(matching_plans)):
            self.allplans.insert(i, matching_plans[i])

    def update_planinfo(self) -> None:
        """Updates plan info panel based on selected name."""
        index_my = self.myplans.curselection() # type: ignore
        index_all = self.allplans.curselection() # type: ignore
        if index_my:
            self.current_plan = self.myplans.get(index_my[0])
            self.show_planinfo()
        elif index_all:
            self.current_plan = self.allplans.get(index_all[0])
            self.show_planinfo()

    def show_planinfo(self) -> None:
        """Displays optional info screen.
        
        Info texts are defined at the beginning of each plan file in 'plans' folder.
        If no valid info string is found, displays a blank screen.
        """
        original = self.current_plan
        with open(gui_paths.PLANS_PATH/(self.current_plan+'.py')) as file_read:
            infolist = file_read.readlines()
        try:
            if infolist[0] == '\"\"\"\n':
                info_comment_end = infolist[1:].index('\"\"\"\n')
                try:
                    with open(gui_paths.FILES_PATH/'time_data.json') as timedata_read:
                        current_version = json.load(timedata_read)[original]["version"]
                except KeyError:
                    current_version = '-'
                core_text = ['[Plan Name] '+original+'\n','[Game Version] '+str(current_version)+'\n']
                core_text.extend(infolist[1:info_comment_end+1])
                readtext = ''.join(core_text)
                self.info_window['state'] = 'normal'
                self.info_window.delete(1.0, tk.END)
                self.info_window.insert('end', readtext)
                self.info_window['state'] = 'disabled'
            else:
                self.info_window['state'] = 'normal'
                self.info_window.delete(1.0, tk.END)
                self.info_window.insert('end', '')
                self.info_window['state'] = 'disabled'
        except IndexError:    
            self.info_window['state'] = 'normal'
            self.info_window.delete(1.0, tk.END)
            self.info_window.insert('end', '')
            self.info_window['state'] = 'disabled'

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
        self.myplans.selection_set(index[0]-1)

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
        self.myplans.selection_set(index[0]+1)

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

    def remove_allcurrentplans(self) -> None:  
        """Remove all currently selected plans from queue."""
        self.myplans.delete(0, "end")
        with open(gui_paths.QUEUE_LIST_PATH, 'w') as _:
            ...

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