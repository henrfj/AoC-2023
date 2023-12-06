"""
The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

"""

seeds = []

def seedy():
    pass

#with open('input.txt', 'r') as f:
#    schematic = [list(line.strip()) for line in f]

with open('test_input.txt', 'r') as f:
    schematic = [list(line.strip()) for line in f]


seeds = seedy(schematic)



print(seeds)
