"""Implements QueueModeWindow class."""

from __future__ import annotations

import itertools as it
import json
import tkinter as tk
from tkinter import ttk

import gui.gui_paths as gui_paths
from gui.gui_tools import os_font
from utils import plan_data

class QueueModeWindow:
    """Gui window where user can modify current list of queued plans.

    Queue data is stored in 'Files/text files/queue_list.txt'.
    """
    def __init__(self) -> None:
        """Initialize queue mode window."""
        self.queuewindow = tk.Toplevel()
        self.queuewindow.title("Queue map list")
        self.queuewindow.iconbitmap(gui_paths.FILES_PATH/'btd6bot.ico')
        self.queuewindow.geometry('930x400+100+550')
        self.queuewindow.minsize(930,400)
        self.queuewindow.maxsize(930,400)
        # hotkeys
        self.queuewindow.bind("<Shift-A>", lambda _: self._add_plan())
        self.queuewindow.bind("<Shift-R>", lambda _: self._remove_plan())
        self.queuewindow.bind("<Shift-U>", lambda _: self._move_up())
        self.queuewindow.bind("<Shift-D>", lambda _: self._move_down())

        self.current_plan: str = ''
        myplanslabel = tk.Label(self.queuewindow, 
                                text='Current queue', 
                                font=os_font)
        myplanslabel.grid(column=0, row=0)

        currentplans_scroll = ttk.Scrollbar(self.queuewindow, 
                                            orient='vertical')
        currentplans_scroll.grid(column=1, row=1, sticky="nsw")

        self.myplans = tk.Listbox(self.queuewindow,
                                    width=36, 
                                    height=20, 
                                    yscrollcommand=currentplans_scroll.set, 
                                    font=os_font)
        self.myplans.grid(column=0, row=1, padx=(11, 0))
        self.myplans.bind("<<ListboxSelect>>", lambda _: self._update_planinfo())
        self.myplans.bind("<KeyPress>", lambda e, list_type=self.myplans: self._searchqueue(e, list_type))
        currentplans_scroll.configure(command=self.myplans.yview)

        self.up = tk.Button(self.queuewindow, 
                            text=u'\u2191\n\n', 
                            width=1, 
                            height=5, 
                            command=self._move_up,
                            font=os_font)
        self.up.grid(column=2, row=1, sticky='n', padx=(2,0))

        self.down = tk.Button(self.queuewindow, 
                                text=u'\n\n\u2193', 
                                width=1,
                                height=5, 
                                command=self._move_down,
                                font=os_font)
        self.down.grid(column=2, row=1, sticky='s', padx=(2,0))
    
        allplans_scroll = ttk.Scrollbar(self.queuewindow, 
                                        orient='vertical')
        allplans_scroll.grid(column=4, row=1, sticky="nsw", padx=(0, 11))

        allplanslabel = tk.Label(self.queuewindow, 
                                text='All plans', 
                                font=os_font)
        allplanslabel.grid(column=3, row=0)

        self.allplans = tk.Listbox(self.queuewindow, 
                                    width=36, 
                                    height=20, 
                                    yscrollcommand=allplans_scroll.set,
                                    font=os_font)
        self.allplans.grid(column=3, row=1, padx=(11, 0))
        self.allplans.bind("<<ListboxSelect>>", lambda _: self._update_planinfo())
        self.allplans.bind("<KeyPress>", lambda e, list_type=self.allplans: self._searchqueue(e, list_type))
        allplans_scroll.configure(command=self.allplans.yview)

        info_window_scroll = ttk.Scrollbar(self.queuewindow, 
                                            orient='vertical')
        info_window_scroll.grid(column=6, row=1, sticky="nsw")

        infolabel = tk.Label(self.queuewindow, 
                            text='Plan info', 
                            font=os_font)
        infolabel.grid(column=5, row=0)

        self.info_window = tk.Text(self.queuewindow, 
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

        self.delbutton = tk.Button(self.queuewindow, 
                                    text='Remove', 
                                    command=self._remove_plan, 
                                    width=10, 
                                    font=os_font)
        self.delbutton.grid(column=0, row=2, sticky="w", padx=(11,0),pady=(5,0))
        
        self.delall_button = tk.Button(self.queuewindow, 
                                        text='Remove all', 
                                        command=self._remove_allcurrentplans, 
                                        width=10, 
                                        font=os_font)
        self.delall_button.grid(column=0, row=2, sticky="e", padx=(11,0), pady=(5,0))

        self.addbutton = tk.Button(self.queuewindow, 
                                    text='Add', 
                                    command=self._add_plan, 
                                    width=10, 
                                    font=os_font)
        self.addbutton.grid(column=3, row=2, sticky="w", padx=(11,0), pady=(5,0))

        self.all_searchbartext = tk.StringVar(value="")
        self.all_searchbartext.trace_add("write", lambda r, w, u: self._callback_all())

        self.all_searchbar = tk.Entry(self.queuewindow, 
                                        textvariable=self.all_searchbartext, 
                                        font=os_font)
        self.all_searchbar.grid(column=3, row=2, sticky="e")
        self.all_searchbar.insert(0, "search plans...")
        self.all_searchbar.bind('<FocusIn>', lambda _: self._clear_entry())
        self.all_searchbar.bind('<FocusOut>', lambda _: self._set_defaultmessage())
        self.all_searchbar.config(fg='gray')

        self._read_queue_list()
        self._read_allplans_list()
        self.all_searchbar.setvar(value="")

    def _clear_entry(self) -> None:
        if self.all_searchbar.get() == 'search plans...':
            self.all_searchbar.delete(0, "end")
            self.all_searchbar.config(fg='black')
        self.myplans.selection_clear(0, 'end')

    def _set_defaultmessage(self) -> None:
        if self.all_searchbar.get() == '':
            index = self.allplans.curselection()
            self.all_searchbar.insert(0, "search plans...")
            self.all_searchbar.config(fg='gray')
            self._read_allplans_list()
            if index != ():
                self.allplans.select_set(index[0])

    def _searchqueue(self, event: tk.Event, list_type: tk.Listbox) -> None:
        _allowed_shiftchars = {'#'} # set of allowed Shift+CHAR combinations in plan names
        values = list_type.get(0, 'end')
        selected = list_type.curselection()
        if selected != ():
            current = selected[0]
            for i in it.chain(range(current + 1, list_type.size()), range(0, current)):
                key = event.char.lower()
                if (key == values[i][0].lower() and 
                    (key in _allowed_shiftchars or event.state != 9)): # event.state == 9 means holding Shift key
                    list_type.select_clear(0, 'end')
                    list_type.select_set(i)
                    list_type.activate(i)
                    list_type.see(i)
                    return

    def _get_plansearchresult(self, searchtext: str) -> list[str]:
        """Add custom search tools.
        
        Commands:
            *v{OPERATOR}{VERSION} {TEXT}
            - {OPERATOR} has values "<", ">", "="
            - {VERSION} is any integer or a dash '-' for plans with no recorded version data.
            - {TEXT} is arbitrary text string
            Searches all plans with specific game version {VERSION} and using {TEXT} to filter items. Space between
            {VERSION} and {TEXT} is required.

            EXAMPLES:  
                *v=50 => has a single space after 50; this finds all plans with game version equal to 50
                *v<51 hard => find all plans with version less than 51 and on hard difficulty
                *v>51 dark castle easy => find all plans with version 51 or higher on dark castle, on easy difficulty
                *v=- => all plans with no recorded version data
        """
        plans_all = plan_data.read_plans()
        plans_found: list[str] = []
        if searchtext[0:2] == "*v" and len(searchtext) >= 5 and searchtext.find(' ') != -1: # *v command
            versioncheck, search = searchtext.split(' ', 1)
            versioncompare: str = versioncheck[2]
            try:
                versionnumber: int = int(versioncheck[3:])
                if versionnumber < 1 or versionnumber > 999:
                    return []
            except ValueError:
                versionnumber: int = versioncheck[3:]
                if versionnumber != '-':
                    return []
            ver: int
            timedata: dict[str, str | int | list[str]]
            with open(gui_paths.FILES_PATH/"time_data.json") as planfile:
                timedata = json.load(planfile)
            for plan_name in plans_all:
                try:
                    ver = timedata[plan_name]["version"]
                except KeyError:
                    ver = '-'
                plan_strat: str = plan_data.return_strategy(plan_name).split('-')
                if (search in plan_name.lower() or 
                    search in plan_name.lower().replace('_', ' ') or
                    search in plan_data.return_map(plan_name)+" "+plan_strat[0].lower()+" "+plan_strat[1].lower()):
                    if ((versioncompare == "<" and isinstance(ver, int) and isinstance(versionnumber, int) and
                         ver < versionnumber) or
                        (versioncompare == ">" and isinstance(ver, int) and isinstance(versionnumber, int) and
                         ver > versionnumber) or
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

    def _highlight_planlist_entry(self, list_type: tk.Listbox, index: int) -> None:
        list_type.select_clear(0, "end")
        if list_type.size() == 0:
            self.info_window['state'] = 'normal'
            self.info_window.delete(1.0, tk.END)
            self.info_window['state'] = 'disabled'
            return
        elif list_type.size() == 1 and index == 0:
            list_type.select_set(index)
            list_type.activate(index)
        elif index < list_type.size()-1:
            list_type.select_set(index)
            list_type.activate(index)
            list_type.see(index)
        else:
            list_type.select_set(index-1)
            list_type.activate(index-1)
            list_type.see(index-1)
        self._update_planinfo()

    def _update_planinfo(self) -> None:
        """Updates plan info panel based on selected plan."""
        index_my = self.myplans.curselection() # type: ignore
        index_all = self.allplans.curselection() # type: ignore
        if index_my != ():
            self.current_plan = self.myplans.get(index_my[0])
            self._show_planinfo()
        elif index_all != ():
            self.current_plan = self.allplans.get(index_all[0])
            self._show_planinfo()

    def _show_planinfo(self) -> None:
        """Displays info screen.
        
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

    def _move_up(self) -> None:
        """Handles moving currently selected queue entry one row up."""
        index = self.myplans.curselection() # type: ignore
        if index != () and index[0] != 0:
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

    def _move_down(self) -> None:
        """Handles moving currently selected queue entry one row down."""
        index = self.myplans.curselection() # type: ignore
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed = file_read.readlines()
        if index != () and index[0] < len(listed)-1:
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

    def _add_plan(self) -> None:
        """Add a new plan to queue.
        
        Won't add a plan if it's already in queue.
        """
        index = self.allplans.curselection() # type: ignore
        if index != ():
            selected_plan = self.allplans.get(index[0])
            with open(gui_paths.QUEUE_LIST_PATH) as file_read:
                listed_plans = plan_data.list_format(file_read.readlines())
            if selected_plan in listed_plans:
                return
            self.myplans.insert(tk.END, selected_plan)
            with open(gui_paths.QUEUE_LIST_PATH, 'a') as file_append:
                file_append.write(self.allplans.get(index[0])+'\n')
            self._callback_all()
            self._highlight_planlist_entry(self.allplans, index[0])

    def _remove_allcurrentplans(self) -> None:  
        """Remove all selected plans from queue."""
        self.myplans.delete(0, "end")
        with open(gui_paths.QUEUE_LIST_PATH, 'w') as _:
            ...
        self._callback_all()
        
    def _remove_plan(self) -> None:
        """Remove selected plan from queue."""
        index = self.myplans.curselection() # type: ignore
        if index != ():
            self.myplans.delete(index[0])    
            with open(gui_paths.QUEUE_LIST_PATH) as file_read:
                listed = file_read.readlines()
            listed.pop(index[0])
            plan_data.list_format(listed)
            with open(gui_paths.QUEUE_LIST_PATH, 'w') as file_write:
                for line in listed:
                    file_write.write(line)
            self._callback_all()
            self._highlight_planlist_entry(self.myplans, index[0])
            
    def _read_queue_list(self) -> None:
        """Load current list of queued plans.
        
        Performs a check for all found plan names to see if they're still available. If not, removes them 
        automatically from queue.
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

    def _read_allplans_list(self) -> None:
        """Load and insert all found plans which are not listed in query into allplans listbox."""
        with open(gui_paths.QUEUE_LIST_PATH) as file_read:
            listed_plans_raw = file_read.readlines()
            listed_plans = plan_data.list_format(listed_plans_raw)
        found_plans = plan_data.read_plans()
        for i in range(0, len(found_plans)):
            if found_plans[i] not in listed_plans:
                self.allplans.insert(i, found_plans[i])

    def get_queuewindow(self) -> tk.Toplevel:
        """Get current queue window.
        
        Returns:
            Current Toplevel window object of QueueModeWindow.
        """
        return self.queuewindow