"""from itertools import combinations

image = open('input.txt').read().splitlines()
empty_rows = [y for y, row in enumerate(image)
              if all(char == '.' for char in row)]
empty_cols = [x for x, cols in enumerate(zip(*image))
              if all(char == '.' for char in cols)]

initial_width = len(image[0])
for row in reversed(empty_rows):
    image.insert(row, '.' * initial_width)

initial_height = len(image)
for col in reversed(empty_cols):
    for row in range(initial_height):
        image[row] = image[row][:col] + '.' + image[row][col:]

galaxy_coords = []
for y, row in enumerate(image):
    for x, char in enumerate(row):
        if char == '#':
            galaxy_coords.append((x, y))


def manhattan_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


shortest_paths = [manhattan_distance(galaxy1, galaxy2)
                  for galaxy1, galaxy2 in combinations(galaxy_coords, 2)]
print(sum(shortest_paths))"""

"""
Cosmic expansion:
- Observatory on the way to the hot springs to find people on metal island.
- . empty space, # galaxies on a star map.
- Sum of lenghts of shortest paths between each pair of galaxies.
=> Space expansion, where no mass is present:  
any rows or columns that contain no galaxies should all actually be twice as big.
=> Then, manhattan distance between each pair of galaxies.
"""

def expand_map(star_map):
    empty_rows = [y for y, row in enumerate(star_map)
                    if all(char == '.' for char in row)]
    empty_cols = [x for x, cols in enumerate(zip(*star_map)) # Transpose rows<->cols
                    if all(char == '.' for char in cols)]
    
    # Reverse traverse star_map and add new cols 

    return 0


def calculate_distances(star_map):
    exanded_map = expand_map(star_map)


    return 0



with open('example_input.txt', 'r') as f:
    star_map = [line.strip() for line in f]


distances = calculate_distances(star_map)



print(distances)