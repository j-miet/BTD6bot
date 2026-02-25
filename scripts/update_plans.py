"""Auto-updates docs/Plans.md file."""

import datetime
from pathlib import Path
import os
import string
    
def return_map(plan: str) -> str:
    newplan = plan.replace('_', ' ')
    for s in newplan:
        if s.isupper():
            return newplan[:newplan.index(s)]
    return ''

def return_strategy(plan: str) -> str:
    diff_start_pos = 0
    mode_start_pos = 0
    try:
        for i in range(0, len(plan)):
            if plan[i].isupper():
                diff_start_pos= i
                for j in range(diff_start_pos+1, len(plan)):
                    if plan[j].isupper():
                        mode_start_pos = j
                        break
                break
        if diff_start_pos == 0 or mode_start_pos == 0:
            return ''
        else:
            return plan[diff_start_pos:mode_start_pos]+'-'+ plan[mode_start_pos:]
    except IndexError:
        return ''

def read_plans() -> list[str]:
    namelist: list[str] = os.listdir(Path(__file__).parent.parent/'btd6bot/plans')
    try:
        namelist.remove('__init__.py')
        namelist.remove('_plan_imports.py')
    except ValueError:
        ...
    try:
        for file_name in namelist[:]:
            if '.py' not in file_name:
                namelist.remove(file_name)
        newlist = [name.replace('.py', '') for name in namelist]
        newlist.sort()
        for plan in newlist:
            if return_map(plan) == '' or return_strategy(plan) == '':
                newlist.remove(plan)
        return newlist
    except ValueError:
        return []

def return_maps_and_strats(data: list[str]) -> dict[str, list[str]]:
    map_strat: dict[str, list[str]] = {}
    for d in data:
        map_name = return_map(d)
        strategy_name = return_strategy(d)
        if map_name != '' and strategy_name != '':
            if map_name in map_strat:
                map_strat[map_name].append(strategy_name)
            else:
                map_strat.update({map_name : [strategy_name]})
    return map_strat

def capitalize(string_val: str) -> str:
    result = string.capwords(string_val).replace('_', ' ')
    first_char = 0
    if not string_val[0].isalpha():
        for char in string_val[1:]:
            if char.isalpha():
                first_char = string_val.index(char)
                break
    if first_char > 0:
            to_list = list(string_val)
            to_list[first_char] = string_val[first_char].capitalize()
            result = ''.join(to_list)
    return result

def sort_by_strat(strat: str) -> int:
    match strat:
        case "Easy-Standard":
            return 0
        case "Easy-Primary":
            return 1
        case "Easy-Deflation":
            return 2
        case "Medium-Standard":
            return 3
        case "Medium-Military":
            return 4
        case "Medium-Apopalypse":
            return 5
        case "Medium-Reverse":
            return 6
        case "Hard-Standard":
            return 7
        case "Hard-Magic":
            return 8
        case "Hard-Double_hp":
            return 9
        case "Hard-Half_cash":
            return 10
        case "Hard-Alternate":
            return 11
        case "Hard-Impoppable":
            return 12
        case "Hard-Chimps":
            return 13
    

INFO = f'''# Supported game plans (Last updated {datetime.date.today()})

- this list is auto-updated using ``scripts/update_plans.py``
- all implemented plans are listed. Each game mode includes
    - link to corresponding .py plan file located in ``plans`` directory
    - the documentation of corresponding .py plan file which is read from the same file

    Some plan names can have invalid symbols which causes their links not to work. One such example is #Ouch with its \\# symbol

---

'''

easy_check = True
medium_check = True
hard_check = True
info_indent: int = 3

plans = read_plans()
plans_dict = return_maps_and_strats(plans)
plans_info: dict[str, list[str]] = {}
for p in plans:
    with open(Path(__file__).parent.parent/'btd6bot/plans'/(p+'.py')) as file_read:
        infolist = file_read.readlines()
    for i in range(0, len(infolist)):
        infolist[i] = infolist[i] + info_indent*'\t'
    plans_info[p] = infolist

with open(Path(__file__).parent.parent/'Plans.md', 'w') as plansfile:
    plansfile.writelines(INFO)
    for plan in plans_dict.keys():
        mapname = capitalize(plan)
        linkname = plan.lower().replace(' ', '-') 
        plansfile.write(f'- [{mapname}](#{linkname})\n')
    plansfile.write('\n')
    
    for plan in plans_dict.keys():
        plansfile.write(f'### {capitalize(plan)}\n')
        plans_ordered = []
        for plan_strat in plans_dict[plan]:
            plans_ordered.append(plan_strat)
        plans_ordered.sort(key=sort_by_strat)
        for strat in plans_ordered:
            if 'Easy' in strat and easy_check:
                plansfile.write('- Easy\n')
                easy_check = False
            elif 'Medium' in strat and medium_check:
                plansfile.write('- Medium\n')
                medium_check = False
            elif 'Hard' in strat and hard_check:
                plansfile.write('- Hard\n')
                hard_check = False
            else:
                ...
            strat_split = strat.split('-')
            planname = f'{plan.replace(' ', '_')}{strat_split[0]}{strat_split[1]}'
            plansfile.write(f'\t- [{strat_split[1]}](btd6bot/plans/{planname}.py)\n')
            try:
                info_comment_end = 0
                if plans_info[planname][0] == '\"\"\"\n'+info_indent*'\t':
                    info_comment_end = plans_info[planname][1:].index('\"\"\"\n'+info_indent*'\t')
                    plansfile.write('\n'+info_indent*'\t')
                    plansfile.writelines(plans_info[planname][1:info_comment_end+1])
                    plansfile.write('\n')
            except IndexError:
                ...
        easy_check, medium_check, hard_check = True, True, True