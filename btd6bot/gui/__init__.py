"""Creates and controls graphical user interface.

Each GUI window is implemented through a class. These classes are

--MainWindow (main_window)--
Main GUI window that has to exist or program will terminate. Other top level windows are created through it
via button presses. Allows the user to choose map and any strategy made for it: first the ocr reader must be 
initialized (see (2) at the bottom of this documentation), then user can move into monitoring window after pressing 
'Open bot window' button. Has also toggleable buttons for 'queue mode', which allows list of plans to be played, and 
'replay mode' that allows infinite repetition of a plan or list of plans, if queue mode is enabled. Finally, there's a 
'Show plot' button which reads the current plan file based on chosen map and plan from 'plan' folder, parses all bot 
commands to a dictionary and displays these commands as a 2D plot to show user a preview of what's done on each round, 
alongside with a few line charts.

--MonitoringWindow (monitoring_window)--
Window that opens after pressing 'Open bot window' button. Is responsible of running and stopping bot.
Standard output is directed to this window during bot runtime to allow tracking all the progress and commands of bot.

--QueueModeWindow (queue_window)--
Allows adding and changing order of plan list that can be played by enabling queue mode. Current list is saved in 'text 
files/queue_list.txt'.

--HotkeyWindow (hotkey_window)--
Allows the user to set their bot hotkeys through interface instead of editing any files manually. These keys are then
updated to 'text files/hotkeys.txt' file to be used later by hotkeys.py module. Displays a help window text read from
'text files/hotkeyhelp.txt'

--HelpWindow (help window)--
Opens a help/readme window. Text is loaded from 'text files/help.txt.'

---

(1) This package relies a lot on text reading/writing and multithreading so precausions are taken to prevent unwanted
behaviour. Importantly:
>all files are closed after their use and each thread operates as individually as possible from one another. 
>after closing any top level window, the closing of corresponding thread is handled automatically and with appropriate 
checks.
    --gui_tools included a thread termination tool + standard output redirecter to MonitoringWindow.

(2) In MainWindow.monitoring_window, an import of OCR_READER constant is included. This reader is required so that
optical character recognition processes during bot runtime are possible, and it's pretty much the only reasonable way
to build an API that allows for communication with the BTD6 game, when modding of game files is out of question.

The reader uses easyocr library which always requires loading the reader to memory. This process takes about 10-15
seconds. Only a single reader object is loaded: it can be then passed as an argument for functions needing it, avoiding 
the need of further inits after first one.
"""