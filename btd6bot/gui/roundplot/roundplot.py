"""Read the map's plan file located in 'plans' folder and creates a subplot out of all round commands.

This allows user to check what commands, on what round and in which order the plan includes.
Ignores lines containing # at any point and also lines having None/pass without anything else (i.e. placeholder lines).
So you can insert comments with #, just add them on separate rows - otherwise entire row is ignored.
Could implement lot of the stuff here using regular expressions but wasn't eager to spend time with them, honestly.


Issues (both old and current):

Plots get laggy very quickly if too much text is added, and become slow to move around. Haven't found a solution to
this as other backends don't fix anything. Good thing is current plots have a slider for round command scrolling which 
behaves much better even with the lag.

FIXED
There's also a mild memory leak problem that is tied to interractive plots: every time you open a plot, it reserves 
some memory for the rest of program runtime and is unable to be freed. So in theory, unless you open and close the plot 
window for like a hundred times, it will not be an issue. But it still annoying.  
>alas, there's an easy solution (which took way too long to implement): multiprocessing. Every time a plot is created, 
it's handled as a new process. When this process closes, it will automatically release all memory! This is because each 
process has its own memory space whereas threads share theirs among others. So in this case, matplotlib has 
issues with running two processes in one thread: handling both gui plot loops simultaneously (and it's not even the gui 
loop, just any program within same thread causes this issue). This results into problems with handling core functions, 
such as freeing any unused memory and thus is the root cause. But with multiprocessing, plotting is completely 
separated from bot program and thus can freely operate. And even if matplotlib had memory issues under new this 
process, it wouldn't matter because after a plot window closes, the process closes and will free any of its allocated 
memory nontheless.

FIXED
>This is for older solution, when the above solution with multiprocessing wasn't used:

To combat the memory issue, I decided to use matplotlib's garbage collector command+ close any open window 
objects: plt.clf() -> plt.close(). This did indeed slow the memory leak accumulation for a bit, so I kept those lines 
of code. For some time, I didn't notice anything as I rarely used plotting function before running the bot. And when 
I started to notice this error occuring, I suspected the problems were related to many other things, like
 -changing gui elements outside main thread (MainWindow.ocr_init),

 -importing modules that would be imported later in program (again, under MainWindow.ocr_init); found someone on 
 stackoverflow who descripted a similar problem and that was the cause,

 -some kind of thread interference between tkinter and matplotlib, as both should run individual threads and preferably 
 on main thread.

After enough time, I started investigating the last option more thoroughly, but for some time, didn't find any 
solution, until the one below. So the problem and solution is as follows:

Problem: after having used 'Show Plot' at least once and creating a new monitoring window resulted shortly after into a 
'RuntimeError: main thread is not in main loop'. 

Solution: It has something to do with this: https://github.com/matplotlib/matplotlib/issues/29198
So if you call matplotlib garbage collector and close the loop i.e. call the following methods and in that order:

    plt.clf()

    plt.close()

then it seems to interfere with tkinter's __del__ method under some part of code, causing
'Tcl_AsyncDelete: async handler deleted by the wrong thread' error on top. This causes current mainloop unable to 
detect itself inside main thread, because it appears tkinter terminates the current main thread, forcing a shutdown.
Now, I'm not quite sure why this did occur when creating a thread under Monitoringwindow.monitoring_window, but not 
under thread-creating methods for other windows.

So just removing those two lines that I added long time ago solved the issue entirely!
"""

import json
import multiprocessing as mp

from matplotlib import rcParams
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import Slider

import gui.roundplot.calculate as calculate
import gui.gui_paths as gui_paths
from set_plan import get_rounds
from utils import plan_data

def find_fre(plan: list[str]) -> int:
    """Finds row index of last command within the first round block.

    If plan has multiple round blocks, return the row before first 'elif current_round...' line. If it has only a 
    single round block, return last row instead.

    Args:
        plan: Current plan as a list, with each row corresponding to line of code.
        
    Returns:
        An index corresponding to value len(plan)-1: len give the length, but actual indexing starts from 0, so 
            substracting 1 gives final row.
    """
    for code_row in range(14, len(plan)):   # range(len(plan)) is ok, but starting from 14 skips non-relevant code.
        if plan[code_row].find('elif current_round == ') != -1:
            return code_row-1
    return len(plan)-1


def append_rounds(plan: list[str], first_r: int, first_r_end: int, round_labels: list[str]
                  ) -> tuple[list[str], list[str]] | tuple[list[list[str]], list[str]]:
    """Adds all round labels and their respective round commands into different lists.
    
    Both lists are filled in order: each index points to a specific round label in round_label and to a list of round 
    commands in rounds. If plan has only BEGIN round block, it's handled separately: round_labels will always get 
    passed with initial value 'BEGIN' as first round must be included in every plan (because of begin() command).
    If plan has multiple rounds, then just like with single round plans, round commands are added to rounds. Then
    all rounds after BEGIN until END are added. This is followed by removing all empty rounds. Finally, a complete 
    tuple of rounds and labels is returned. 

    Args:
        plan: Currently selected plan after unused code rows are removed.
        first_r: Row number of where first round starts in plan.
        first_r_end: Row number where first round block ends in plan.
        round_labels: List of round numbers.

    Returns:
        rounds, round_labels: A tuple where first element is the list of all round commands, each corresponding to a
            list of commands in round_labels. Second tuple element is for all round labels (numbers + BEGIN/END text) 
            in the plan that have commands included; empty rounds (rounds with commands #, '...' or no code at all) are 
            excluded.
    """
    temp = []
    temp2: list[list[str]] = []
    rounds: list[list[str]] = []
    if len(plan)-1 == first_r_end:  # if plan has only first round block, nothing else.
        for index in range(first_r+1, first_r_end+1):   # everything included on the first round.
            temp.append(plan[index])
        rounds.append(temp)  # adds all commands of a round as a sublist
        return rounds, round_labels
    else:
        current_r = first_r_end+1   # points to first 'elif current_round == ...' line.
        for index in range(first_r+1, current_r):   # everything included on the first round
            temp.append(plan[index])
        rounds.append(temp)  # adds all commands from a round as a sublist
        round_labels.append(plan[current_r].split('== ')[1][:-1])  # remove ':' at the end by not including index -1.
        for line in plan[current_r+1:]: # then rounds between first and last, last included
            if line.startswith('elif current_round =='):
                templist = []
                round_labels.append(line.split('== ')[1][:-1])  # separate round number
                next_line = plan.index(line)
                for index in range(current_r+1, next_line):
                    templist.append(plan[index])
                temp2.append(templist)
                current_r = next_line
        temp2.append(plan[current_r+1:])

        for row in temp2[:]: # remove empty rows. 
            if row == []:
                temp2.remove(row)
        rounds += temp2    
        return rounds, round_labels

def remove_empty_rows(plan: list[str], first_r: int, round_labels: list[str]) -> list[str]:
    """Removes round labels from all corresponding empty round blocks, preventing any empty rounds showing up in plots.
    
    Compares two consecutive code rows: if first contains the latters when latter has "if current_round" in it, it 
    means the first is a round block without any code inside it. And thus, the index of first is found by splitting 
    from the '==' sign (with one space after so '== ') and removing the ':' at the end, then finding corresponding 
    round label index from list of all labels and then removing it.

    Args:
        plan: Plan string, each string corresponds to a line of code.
        first_r_end: Index that points to last code line inside first round block.
        round_labels: Labels of all
        
    Returns:
        new_labels: Filtered label list.
    """
    new_labels = round_labels[:]
    for index in range(first_r, len(plan)):
        if plan[index].find(plan[index-1].split('== ')[0]) != -1:
            try:
                new_labels.pop(new_labels.index(plan[index-1].split('== ')[1][:-1]))
            except IndexError:
                ...
    return new_labels

def plot(round_labels: list[str], rounds: list[str] | list[list[str]], plan_name: str) -> None:
    """Creates subplots to plot round commands and time spent, for each round.
    
    Time plot is static and cannot be interacted with. It loads values from a json file.

    Round command plot is interractive, with rounds on x-axis and round commands on y-axis: a slider is used to jump 
    around rounds and it's updated by calling an inner function 'update' and passed as an argument to on_changed 
    method of slider. This plot will not display empty rounds i.e. rounds without actual commands, and needs the list 
    rounds_labels which does not include them.
   
    Args:
        round_labels: A list of all round numbers where corresponding round has at least one command.
        rounds: A list containing either commands of a single round, or list of all round commands, each an inner list.
        plan_name: Current plan name, required for displaying name inside plot window.
    """
    plt.rcParams['toolbar'] = 'None'
    plt.style.use('dark_background')    # has to be set before any text is inserted.
    fig = plt.figure()
    plt.axis('off')
    fig.gca().get_yaxis().set_visible(False)
    fig.gca().get_xaxis().set_visible(False)
    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.99, top=0.9, wspace=None, hspace=None)
    rcParams['toolbar'] = 'None'
    winmanager = plt.get_current_fig_manager()
    winmanager.window.state('zoomed') # type: ignore
    fig.suptitle(f'Round commands and round times of current plan "{plan_name}".')

    # TODO: Axis 'income and costs'
    #costs = calculate.get_costs(plan_name, round_labels, rounds)
    # incomes = calculate.get_incomes(round_labels, rounds)
    #ax_money = fig.add_subplot(gs[0,0])
    #ax_money.ticklabel_format(style='plain', useOffset=False)
    #f = [t for t in all_labels]
    #ax_money.set_xlabel('[WORK IN PROGRESS]')
    #ax_money.set_ylabel(' ')
    #ax_money.plot(all_labels, f, 'o--')

    # Axis 'round times'
    try:
        # move this block starting here...
        with open(gui_paths.FILES_PATH/'time_data.json') as f:
            time_data = json.load(f)[plan_name]
        plan_rounds: list[str] = time_data["rounds"]
        plan_times: list[str] = time_data["times"]
        plan_times_in_seconds: list[int] = []
        for t in plan_times:
            t_str = t.split(':')
            mins = int(t_str[0])
            secs = int(t_str[1])
            t_in_seconds = mins*60+secs
            plan_times_in_seconds.append(t_in_seconds)
        # ...and ending here, under calculate.py.
        # Return the values plan_times_in_seconds & time_data["time_total"]

        ax_time = fig.add_subplot(2,1,1)
        ax_time.set_title(f'Round times - Total: {time_data["time_total"]}')
        ax_time.set_xlabel('Rounds')
        ax_time.set_ylabel('Round length (seconds)')
        ax_time.plot(plan_rounds, plan_times_in_seconds, 'o:', label='Round length')
        ax_time_legend = ax_time.legend(loc='upper left', edgecolor='black')
        ax_time_legend.get_frame().set_alpha(None)
        ax_time_legend.get_frame().set_facecolor((0,0,1,0.1))
        # set_major_locator is used for setting equally spaced labels on x-axis. Currently all modes except impoppable 
        # and chimps can fit their labels just fine, but for those two, some form of densing is required. The question 
        # is: what line length will ensure that starting from round 6 label, equally spaced lines will land just on top 
        # of round 100 label. The answer is in this case is easy and it's 2. Why? See explanations below.
        #
        # x-axis has N rounds => it takes N-1 steps to traverse from first point to last if step length=1.
        # Then plt.MaxNLocator(K, nums), in this context, answers the following question:
        # what is the shortest integer step length L that can reach from first point to last in up to K steps,
        # and L is an element of 'nums' (=all allowed step lengths, up to 10)
        #
        # >A mathematical formulation:
        # L>=1, K <= N-1
        # smallest value of L such that kL >= N with k<=K <=> L=N/n >= N/K. And as L is to be an integer, choose
        # ceil(N/K). Then find min{a in 'nums' : a >= ceil(N/K)}
        #
        # so if N=40, K=9, nums=[2,3,6,7] => ceil(N-1/K) = 5, but 5 not in nums, thus next smallest is 6.
        #
        # >What are all possible step lengths that land just at point N?
        # 1+kL = N => k = (N-1)/L
        # k = N-1/L > 1 AND k is integer ==> is L a factor N-1 i.e. L = (N-1)/k for some k <= K?
        #
        # to apply this in practise: allow up to K=N-1 steps and check factors:
        # N=40 => find all factors of N-1=39 => 39=3*13. This means:
        # 3 steps of length 13 OR 13 steps of length 3 lands exactly on top of last point.
        #
        # >currently, only problematic rounds are the longest: impoppable and chimps both have 95 rounds, and fitting 
        # all 95 one after another won't do -> this means factor 1 won't suffice so find the next smallest:
        # N=95, N-1=94 has factors 2, 47, 94. So 2 happens to be next, and it's also the only one being <= 10.
        if len(plan_rounds)  == 95:
            ax_time.xaxis.set_major_locator(MaxNLocator(len(plan_rounds)-1, steps=[2]))
    except KeyError:
        ax_time = fig.add_subplot(2,1,1)
        ax_time.set_title(f'NO RECORDED TIME DATA FOUND')
        ax_time.set_axis_off()

    # Axis 'round commands'
    ax_rounds = fig.add_subplot(2,5,(7,9))
    ax_rounds.set_title(f'Round commands - '
                        'Order of command execution is top to bottom. Rounds without commands are not included.')
    ax_rounds.get_yaxis().set_visible(False)
    for (x, r) in zip(round_labels, rounds):
        lines = ''
        ax_rounds.bar(x, height=0.1, width=0) # width=0 prevents drawing a visible bar
        if len(r) > 19:
            for text_line in range(0, 14):
                lines += r[text_line]+'\n'
            lines += '.\n.\n.\n'
            lines += r[-2]+'\n'
            lines += r[-1]+'\n'
        else:
            for text_line in range(0, len(r)):
                lines += r[text_line]+'\n'
        ax_rounds.text(x, -0.8, lines, ha='left') # type: ignore

    axis_position = plt.axes((0.1, 0.025, 0.8, 0.025))
    slider_min_val = -0.1
    slider_max_val = len(round_labels)-1+slider_min_val
    if slider_min_val == slider_max_val:
        slider_max_val = slider_min_val-0.01
    round_slider = Slider(axis_position, 'Round slider', slider_min_val, slider_max_val, valinit=0, valstep=1, 
                          initcolor='none')
    # list of steps in slider: used in creating vertical lines on top of slider object.
    vlines_list: list[float] = [slider_min_val + index for index in range(0, round(slider_max_val)+1)]
    axis_position.vlines(vlines_list, 0, 0.5)

    ax_rounds.axis((slider_min_val+0.08, slider_min_val+0.35, -1.0, 2.0))
    round_slider.valtext.set_visible(False) # hide slider value: as empty rounds are not displayed, shows wrong value.

    def update(val: float) -> None:
        #Updates rounds axis (=in this case, round text position) based on current slider position.
        pos = val
        ax_rounds.axis((pos+0.08, pos+0.35, -1.0, 2.0))
        fig.canvas.draw_idle()

    round_slider.on_changed(update)
    plt.show()


def plot_plan(plan_str: str) -> None:
    """Creates a matplotlib round plot chart of currently selected plan.

    *Important* Plot window is created as a separate process via multiprocessing so bot stays unresponsive while window 
    is open; remember to close after you're done!  
        -Why multiprocessing? Matplotlib has a severe memory leak issue with interractive plots: plots should run in 
        main thread but so does the bot. This creates issue with freeing memory after plot is closed. So far the only 
        solution that works is to create a separate process, with its own memory space and let it finish. This way 
        memory allocation is not saved under main process (the bot) and gets all freed after a window is closed.

    X-axis has round labels that have at least a single command included; empty ones are not included.
    Y-axis has all commands of each round listed from top to bottom.

    Delegates most of the responsibilities to other functions; however, it does perform
        -initial plan file check and reading all lines of code from it,
        -removal of all rows of code that have
            -->comments, or even a single symbol # anywhere
            -->'...' string i.e. empty round blocks.
    Any empty round blocks are removed later within remove_empty_row. But before that, all rounds and their respective 
    labels are appended into separate lists. Note that this process would be far easier to handle with dictionaries, 
    but it is what it is (for now).

    Args:
        plan: Plan name.
    """
    with open(gui_paths.PLANS_PATH/(plan_str+'.py')) as file_read:
        try:
            get_plan = plan_data.list_format(file_read.readlines())
        except FileNotFoundError:
            print(f'Can\'t find current plan {plan_str}.')  
            return
    for s in get_plan[:]:   # slicing creates a copy; otherwise removing rows could skip over non-empty ones
        if s.find('#') != -1 or s.find('...') != -1: # remove commented lines
            get_plan.remove(s)

    # get first and final round values as integers instead of BEGIN and END literals.
    strat_name = plan_data.return_strategy(plan_str).split('-')
    if strat_name[1][-1] in (str(i) for i in range(2,10)):
        first_round_num, final_round_num = get_rounds(strat_name[0].upper(), strat_name[1].upper()[:-1])
    else:
        first_round_num, final_round_num = get_rounds(strat_name[0].upper(), strat_name[1].upper())

    first_round = get_plan.index('if current_round == BEGIN:')
    first_round_end = find_fre(get_plan)
    round_labels = [str(first_round_num)]
    rounds, round_labels = append_rounds(get_plan, first_round, first_round_end, round_labels)
    round_labels = remove_empty_rows(get_plan, first_round, round_labels)
    if round_labels[-1] == 'END':
        round_labels.pop()
        round_labels.append(str(final_round_num))
    plot_process = mp.Process(target=plot, args=[round_labels, rounds, plan_str])
    plot_process.start()