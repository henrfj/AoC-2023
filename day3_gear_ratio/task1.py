

def find_sum_of_parts(schematic):
    # Initialize sum of part numbers
    sum_parts = 0

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
                            if 0 <= x < len(schematic) and 0 <= y < len(schematic[0]) and schematic[x][y] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                sum_parts += int(number)
                                break
                    number = ""  # Reset current number
    return sum_parts

with open('input.txt', 'r') as f:
    schematic = [list(line.strip()) for line in f]


sum_of_parts = find_sum_of_parts(schematic)

print(sum_of_parts)
