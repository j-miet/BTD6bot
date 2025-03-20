"""All currently implemented plans.

--Why is the plan file naming system implemented in map_nameDifficultyMode format:
    'map name' is just name of a game map.
    'strategy/strat' refers to map's difficulty and game mode settings combined e.g. Easy Standard, Medium Reverse, etc.
    'plan' refers to a step-by-step process of starting and finishing a single bot loop, all the way from game menu
        to actual game and back to menu, on given map and strategy. On code level, this is equal to running a plan .py
        file and finishing all code, then returning back to GUI.

    ==>You can actually add any number in range 2-9 at the end of plan file e.g. logsEasyStandard5. This means 
       that up to 9 different plans can be made for any single map + strategy.

        This naming format makes working with plan data easy, both in GUI environment and when running the 
        bot itself through a .py plan file. To actually enforce it, a plan name needs to have easily separable
        components for each map name, difficulty and game mode. I just chose the current format as:
            >map name is lowercase and spaces are replaced with underscore _.

            >strategy component has two separate words, both always starting with uppercase letter and ending with
            lowercase. First word points to Difficulty, second to game Mode.

--Why are plans written as .py and not as, say, json or other format of data storing:
    Monkeys and heroes are created through classes and commanded using their own instance methods. Class objects 
    only persist within their local scope, meaning only reasonable way to both store them and call methods on them is under same module, in this case the .py plan file.
---
*Uncomment the code below and add it outside the docstring if plans.module imports need it:
---

#from os.path import dirname, basename, isfile, join
#import glob
#modules = glob.glob(join(dirname(__file__), "*.py"))
#__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
"""