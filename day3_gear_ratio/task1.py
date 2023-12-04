"""
Add up all the "part numbers" in the engine schematic.

Any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.

"""
testing = True
if testing:
    schematics =    ["..35..633.",
                    "......#...",
                    "617*......",
                    ".....+.58.",
                    "..592.....",
                    "......755.",
                    "...$.*....",
                    ".664.598.."]
    line_1 = "467..114..",
    line_2 = "...*......",

else:
    schematics = open('input.txt', 'r')
    #
    line_1 = schematics.readline()
    line_2 = schematics.readline()
    #



for line in schematics:
    break

print(line_1 + "\n" + line_2 + "\n" + line)