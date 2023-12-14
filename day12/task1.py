"""
Hot springs-

- Input is spring condition. Repair damaged records.
- One spring on each row. "." operational, "#" damaged, "?" unknown. 
- But some duplicates - look at numbers.

=> ?###???????? 3,2,1 can be 10 differen arrangements of "." and "#".
    - Group of 3 damaged, group of 2 damaged and group of 1 damaged.
    - .###.##....# is one solution.
    - How many solutions exist?
"""

from tqdm import tqdm



def viable_solution(symbols, groups):
    
    groups_ = []
    group_count = 0
    in_group = False
    for c in symbols:
        if c =="#":
            in_group = True
            group_count += 1

        elif c == "." and in_group:
            in_group = False
            groups_.append(group_count)
            group_count = 0
    if in_group:
        groups_.append(group_count)

    return groups_ == groups

def recursive_solve(symbols, groups, idx = 0, group_index = 0, group_count = 0, in_group = False):
    """
    This function solves the given row using backtracking.

    Parameters:
    symbols: a row from the spring schematics.
    groups: a list of integers representing the groups of '#'.
    idx: the current index in the row.
    group_index: the current index in the groups.
    group_count: the count of '#' in the current group.
    """
    # possible solutions, found downstream of this call
    possible_solutions = 0

    # End of row and last group
    if idx == len(symbols):
        if viable_solution(symbols, groups):
            return 1
        else:
            return 0
    

    # NOTE catches almost all cases, but includes some impossible solutions
    # If the current character is unknown, we branch
    # Prune the space first
    if symbols[idx] == '?':
        # "#" # NOTE: only possible if more groups available, or more room in group!
        if group_index < len(groups) and group_count < groups[group_index]:

            possible_solutions += recursive_solve(symbols[:idx]+["#"]+symbols[idx+1:], groups, idx + 1, group_index, group_count + 1, in_group=True)
        
        # "." # NOTE cannot break up a group still counting
        if in_group and group_count == groups[group_index]: # Break group

            possible_solutions += recursive_solve(symbols[:idx]+["."]+symbols[idx+1:], groups, idx + 1, group_index + 1, group_count = 0, in_group=False)
        elif not in_group: 

            possible_solutions += recursive_solve(symbols[:idx]+["."]+symbols[idx+1:], groups, idx + 1, group_index, group_count = 0, in_group=False)
        

    else: # Character is already set, "#" or "."
        if symbols[idx] == '#':
            if group_index == len(groups): # already exhausted all groups
                return possible_solutions  # No more possible solutions down this path
            # Add count to group
            possible_solutions += recursive_solve(symbols, groups, idx + 1, group_index, group_count + 1, in_group=True)
        else: # '.'
            if in_group: # Break group
                possible_solutions += recursive_solve(symbols, groups, idx + 1, group_index + 1, group_count = 0, in_group=False)
            else: 
                possible_solutions += recursive_solve(symbols, groups, idx + 1, group_index, group_count = 0, in_group=False)
     
    """
    # Brute force
    # Two solutions:
    if symbols[idx] == '?':
        
        #symbols[idx]="#"
        possible_solutions += recursive_solve(symbols[:idx]+["#"]+symbols[idx+1:], groups, idx + 1)
        
        #symbols[idx]="."
        possible_solutions += recursive_solve(symbols[:idx]+["."]+symbols[idx+1:], groups, idx + 1)
    
    else:
        possible_solutions += recursive_solve(symbols, groups, idx + 1)
    """

    return possible_solutions

def possible_solutions(schema : list[str]) -> int:
    """
        
    """
    s = 0
    for i in tqdm(range(len(schema))):
        row = schema[i]
        symbols, numbers  = row.split(" ")
        symbols = list(symbols)
        groups = list(map(int, numbers.split(",")))
        
        s += recursive_solve(symbols, groups)

    return s


def possible_solutions_2(schema : list[str]) -> int:
    """
        
    """
    s = 0
    for i, row in enumerate(schema):
        symbols, numbers  = row.split(" ")
        symbols = list(symbols)
        groups = list(map(int, numbers.split(",")))
        
        
        symbols = symbols + ["?"] + symbols + ["?"] + symbols + ["?"] + symbols+ ["?"] + symbols
        groups = groups * 5

        #print(symbols)
        #print(groups)
        print(f"{i}: {s}", end="\n")
        s += recursive_solve(symbols, groups)
        
    return s





with open('example_input.txt', 'r') as f:
    schema = [line.strip() for line in f]

with open('input.txt', 'r') as f:
    schema = [line.strip() for line in f]


#solution = possible_solutions(schema)
solution = possible_solutions_2(schema)

print(solution)