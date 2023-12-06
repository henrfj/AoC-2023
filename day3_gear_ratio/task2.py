"""
The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

"""

schematic = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]

def find_gear_ratios(schematic):
    # Initialize sum of part numbers
    gear_dict = {}

    # Traverse the 2D list
    for i in range(len(schematic)):
        number = ""  # Initialize current number
        for j in range(len(schematic[0])):
            if schematic[i][j].isdigit():
                # Add digit to current number
                number += schematic[i][j]
                # If it's the end of the line or next cell is not a digit, check if current number is a part
                if j == len(schematic[0]) - 1 or not schematic[i][j + 1].isdigit():
                    # Check the 8 surrounding cells of the first and last digit of the number
                    for di in [-1, 0, 1]:

                        for dj in range(-len(number), 2, 1):
                            x = i + di
                            y = j + dj
                            #
                            if 0 <= x < len(schematic) and 0 <= y < len(schematic[0]) and schematic[x][y] == "*":
                                try:
                                    gear_dict[(x, y)].append(number) 
                                except KeyError:
                                    gear_dict[(x, y)] = [number]
                                break
                    number = ""  # Reset current number
    return gear_dict

with open('input.txt', 'r') as f:
    schematic = [list(line.strip()) for line in f]


gear_dict = find_gear_ratios(schematic)

sum_of_ratios = 0
for k in gear_dict.keys():
    if len(gear_dict[k]) == 2:
        sum_of_ratios += int(gear_dict[k][0]) * int(gear_dict[k][1])


print(sum_of_ratios)
