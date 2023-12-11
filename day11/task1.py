"""
Cosmic expansion:
- Observatory on the way to the hot springs to find people on metal island.
- . empty space, # galaxies on a star map.
- Sum of lenghts of shortest paths between each pair of galaxies.
=> Space expansion, where no mass is present:  
any rows or columns that contain no galaxies should all actually be twice as big.
=> Then, manhattan distance between each pair of galaxies.
"""

import numpy as np
# TODO
# - Dont actually expand map, just +1 when crossing a column / row that is empty.
# - part 2: +1000000 instead, ez pz.
# - manhattan distance? |x1 - x2| + |y1 - y2| + (1)*(all empty rows / col crossed) between.


def expand_map(star_map):
    empty_rows = [y for y, row in enumerate(star_map)
                    if all(char == '.' for char in row)]
    empty_cols = [x for x, cols in enumerate(zip(*star_map)) # Transpose rows<->cols
                    if all(char == '.' for char in cols)]
    
    return empty_rows, empty_cols


def calculate_distances(star_map, expand_factor = 1):
    empty_rows, empty_cols = expand_map(star_map)
    # Find all galaxies
    galaxies = []
    for row, _ in enumerate(star_map):
        for col, _ in enumerate(star_map[row]):
            if star_map[row][col] == "#":
                galaxies.append((row, col))
    # Calculate all distances
    s_dist = np.int64(0) # int 32 not big enouth
    for i, galaxy in enumerate(galaxies[:-1]):
        for other_galaxy in galaxies[i:]:
            #
            distance = np.abs(galaxy[0] - other_galaxy[0]) + np.abs(galaxy[1] - other_galaxy[1])
            # add extra distance from expansion
            for row in empty_rows:
                if other_galaxy[0] < row < galaxy[0] or other_galaxy[0] > row > galaxy[0]:
                    distance += expand_factor-1
            for col in empty_cols:
                if other_galaxy[1] < col < galaxy[1] or other_galaxy[1] > col > galaxy[1]:
                    distance += expand_factor-1
            #
            s_dist += distance
    return s_dist

with open('example_input.txt', 'r') as f:
    star_map = [line.strip() for line in f]

with open('input.txt', 'r') as f:
    star_map = [line.strip() for line in f]


distances = calculate_distances(star_map, expand_factor=2)

print(distances)