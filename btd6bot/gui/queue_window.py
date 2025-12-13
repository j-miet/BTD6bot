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

        self.current_plan: str = ''
        self.myplanslabel = tk.Label(self.queue_optionwindow, 
                                     text='Current queue', 
                                     font=os_font)
        self.myplanslabel.grid(column=0, row=0)
        currentplans_scroll = ttk.Scrollbar(self.queue_optionwindow, 
                                            orient='vertical')
        currentplans_scroll.grid(column=1, row=1, sticky="nsw")
        self.myplans = tk.Listbox(self.queue_optionwindow,
                                  width=36, 
                                  height=20, 
                                  yscrollcommand=currentplans_scroll.set, 
                                  font=os_font)
        self.myplans.grid(column=0, row=1, padx=(11, 0))
        self.myplans.bind("<<ListboxSelect>>", lambda _: self.update_planinfo())
        currentplans_scroll.configure(command=self.myplans.yview)

        self.up = tk.Button(self.queue_optionwindow, 
                            text=u'\u2191\n\n(u)', 
                            width=2, 
                            height=5, 
                            command=self.move_up,
                            font=os_font)
        self.up.grid(column=2, row=1, sticky='n', padx=(2,0))
        self.queue_optionwindow.bind("u", lambda _: self.move_up())

        self.down = tk.Button(self.queue_optionwindow, 
                              text=u'(d)\n\n\u2193', 
                              width=2, 
                              height=5, 
                              command=self.move_down,
                              font=os_font)
        self.down.grid(column=2, row=1, sticky='s', padx=(2,0))
        self.queue_optionwindow.bind("d", lambda _: self.move_down())
    
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
        allplans_scroll.configure(command=self.allplans.yview)
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

        self.delbutton = tk.Button(self.queue_optionwindow, 
                                   text='Remove (r)', 
                                   command=self.remove_plan, 
                                   width=10, 
                                   font=os_font)
        self.delbutton.grid(column=0, row=2, sticky="w", padx=(11,0),pady=(5,0))
        self.queue_optionwindow.bind("r", lambda _: self.remove_plan())
        self.delall_button = tk.Button(self.queue_optionwindow, 
                                       text='Remove all', 
                                       command=self.remove_allcurrentplans, 
                                       width=10, 
                                       font=os_font)
        self.delall_button.grid(column=0, row=2, sticky="e", padx=(11,0), pady=(5,0))
        self.addbutton = tk.Button(self.queue_optionwindow, 
                                   text='Add (a)', 
                                   command=self.add_plan, 
                                   width=10, 
                                   font=os_font)
        self.addbutton.grid(column=3, row=2, sticky="w", padx=(11,0), pady=(5,0))
        self.queue_optionwindow.bind("a", lambda _: self.add_plan())

        self.all_searchbartext = tk.StringVar(value="")
        self.all_searchbartext.trace_add("write", lambda r, w, u: self._callback_all())
        self.all_searchbar = tk.Entry(self.queue_optionwindow, 
                                      textvariable=self.all_searchbartext, 
                                      font=os_font)
        self.all_searchbar.grid(column=3, row=2, sticky="e")
        self.all_searchbar.insert(0, "search plans...")
        self.all_searchbar.bind('<FocusIn>', lambda _: self._clear_entry())
        self.all_searchbar.bind('<FocusOut>', lambda _: self._set_defaultmessage())
        self.all_searchbar.config(fg='gray')

        self.read_queue_list()
        self.read_allplans_list()
        self.all_searchbar.setvar(value="")

    def _clear_entry(self) -> None:
        if self.all_searchbar.get() == 'search plans...':
            self.all_searchbar.delete(0, "end")
            self.all_searchbar.config(fg='black')

    def _set_defaultmessage(self) -> None:
        if self.all_searchbar.get() == '':
            self.all_searchbar.insert(0, "search plans...")
            self.all_searchbar.config(fg='gray')
            self.read_allplans_list()

    def _get_plansearchresult(self, searchtext: str) -> list[str]:
        """Add custom search tools.
        
        Commands:
            *v{OPERATOR}{VERSION} {TEXT}
            - {OPERATOR} has values "<", ">", "="
            - {VERSION} is any integer
            - {TEXT} is arbitrary text string
            Searches all plans with specific game version {VERSION} and using {TEXT} to filter items. Space between
            {VERSION} and {TEXT} is required.

            EXAMPLES:  
                *v=50 => has a single space after 50; this finds all plans with game version equal to 50
                *v<51 hard => find all plans with version less than 51 and on hard difficulty
                *v>51 dark castle easy => find all plans with version 51 or higher on dark castle, on easy difficulty
        """
        plans_all = plan_data.read_plans()
        plans_found: list[str] = []
        if searchtext[0:2] == "*v" and len(searchtext) >= 5 and searchtext.find(' ') != -1: # *v command
            versioncheck, search = searchtext.split(' ', 1)
            versioncompare: str = versioncheck[2]
            versionnumber: int = int(versioncheck[3:])
            ver: int
            timedata: dict[str, str | int | list[str]]
            with open(gui_paths.FILES_PATH/"time_data.json") as planfile:
                timedata = json.load(planfile)
            for plan_name in plans_all:
                ver = timedata[plan_name]["version"]
                plan_strat: str = plan_data.return_strategy(plan_name).split('-')
                if (search in plan_name.lower() or 
                    search in plan_name.lower().replace('_', ' ') or
                    search in plan_data.return_map(plan_name)+" "+plan_strat[0].lower()+" "+plan_strat[1].lower()):
                    if ((versioncompare == "<" and ver < versionnumber) or
                        (versioncompare == ">" and ver > versionnumber) or
                        (versioncompare == "=" and ver == versionnumber)):
                        plans_found.append(plan_name)
        else:
            for plan_name in plans_all:
                plan_strat: str = plan_data.return_strategy(plan_name).split('-')
                if (searchtext in plan_name.lower() or 
                    searchtext in plan_name.lower().replace('_', ' ') or
                    searchtext in plan_data.return_map(plan_name)+" "+plan_strat[0].lower()+" "+plan_strat[1].lower()):
                    plans_found.append(plan_name)
        return plans_found

    def _callback_all(self) -> None:
        searchtext = self.all_searchbartext.get().lower()
        if searchtext == "search plans..." and self.all_searchbar.cget("fg") == "gray":
            searchtext = ""
        matching_plans = self._get_plansearchresult(searchtext)
        self.allplans.delete(0, "end")
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed_plans_raw = file_read.readlines()
            listed_plans = plan_data.list_format(listed_plans_raw)
        for i in range(0, len(matching_plans)):
            if matching_plans[i] not in listed_plans:
                self.allplans.insert(i, matching_plans[i])

    def _highlight_allplans_entry(self, index: int) -> None:
        self.allplans.select_clear(0, "end")
        if self.allplans.size() == 0:
            self.info_window['state'] = 'normal'
            self.info_window.delete(1.0, tk.END)
            self.info_window['state'] = 'disabled'
            return
        elif index < self.allplans.size()-1:
            self.allplans.select_set(index)
            self.allplans.activate(index)
        else:
            self.allplans.select_set(index-1)
            self.allplans.activate(index-1)
        self.update_planinfo()

    def _highlight_myplans_entry(self, index: int) -> None:
        self.myplans.select_clear(0, "end")
        if self.myplans.size() == 0:
            self.info_window['state'] = 'normal'
            self.info_window.delete(1.0, tk.END)
            self.info_window['state'] = 'disabled'
            return
        elif index < self.myplans.size()-1:
            self.myplans.select_set(index)
            self.myplans.activate(index)
        else:
            self.myplans.select_set(index-1)
            self.myplans.activate(index-1)
        self.update_planinfo()

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
        self.myplans.activate(index[0]-1)
        self.myplans.see(index[0]-1)

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
        self.myplans.activate(index[0]+1)
        self.myplans.see(index[0]+1)

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
        self._callback_all()
        self._highlight_allplans_entry(index[0])

    def remove_allcurrentplans(self) -> None:  
        """Remove all currently selected plans from queue."""
        self.myplans.delete(0, "end")
        with open(gui_paths.QUEUE_LIST_PATH, 'w') as _:
            ...
        self._callback_all()
        
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
        self._callback_all()
        self._highlight_myplans_entry(index[0])
            
    def read_queue_list(self) -> None:
        """Load an existing list of queued plans.
        
        Will also check whether all currently queued plans are found. If not, removes them automatically.
        """
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed_plans_raw = file_read.readlines()
            listed_plans = plan_data.list_format(listed_plans_raw)
        all_plans = plan_data.read_plans()
        if listed_plans != [] and set(listed_plans).issubset(set(all_plans)):
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
        """Load a list of all existing plans which are not selected in current query."""
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed_plans_raw = file_read.readlines()
            listed_plans = plan_data.list_format(listed_plans_raw)
        found_plans = plan_data.read_plans()
        for i in range(0, len(found_plans)):
            if found_plans[i] not in listed_plans:
                self.allplans.insert(i, found_plans[i])

    def get_optionwindow(self) -> tk.Toplevel:
        """Get current option window.
        
        Returns:
            Current Toplevel window object of QueueModeWindow.
        """
        return self.queue_optionwindow