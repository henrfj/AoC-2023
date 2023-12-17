"""
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.


"""
from numba import jit
import numpy as np

@jit(nopython=True)
def str2int(text):
    c_min = ord("0")
    c_max = ord("9")
    n = len(text)
    valid = n > 0
    # determine sign
    start = n - 1
    stop = -1
    sign = 1
    if valid:
        first = ord(text[0])
        if first == ord("+"):
            stop = 0
        elif first == ord('-'):
            sign = -1
            stop = 0
    # parse rest
    number = 0
    j = 0
    for i in range(start, stop, -1):
        c = ord(text[i])
        if c_min <= c <= c_max:
            number += (c - c_min) * 10 ** j
            j += 1
        else:
            valid = False
            break
    return sign * number if valid else None

@jit(nopython=True)
def seedy(seed_mapps : list[list], seeds) -> int:

    src_ranges = []
    dst_ranges = []
    for _, line in enumerate(seed_mapps[3:]):
        if ""==line or "end"==line:
            for i, seed in enumerate(seeds): #SRC
                #
                for idx, (start, stop) in enumerate(src_ranges):
                    if start <= seed < stop:
                        dist_from_start = seed-start

                        seeds[i] = dst_ranges[idx][0] + dist_from_start
                        break  

            src_ranges = []
            dst_ranges = []

        elif "-to-" in line:
            continue
        else:
            l = line.split(" ")
            # Extract useful info
            dst_start = str2int(l[0])
            src_start = str2int(l[1])
            range_ = str2int(l[2])
            #
            src_ranges.append((src_start, src_start+range_))
            dst_ranges.append((dst_start, dst_start+range_))

    return min(seeds)

@jit(nopython=True)
def all_seeds(seed_maps, seeds):
    #
    min_location = None
    #
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        range_ = seeds[i+1]
        location = seedy(seed_maps, [i for i in range(start, start+range_)])
        #
        if min_location == None or location < min_location:
            min_location = location
    #
    return min_location


with open('test_input.txt', 'r') as f:
    seed_maps = [line.strip() for line in f]

#with open('input.txt', 'r') as f:
#    seed_maps = [line.strip() for line in f]

seeds = seed_maps[0].split(": ")[-1].strip().split(" ")
seeds = [int(s) for s in seeds]
location = all_seeds(seed_maps, seeds)

print(location)

# TODO
#   - New method: just follow the seeds through the layers - dont produce a "full map first"
#   - Use List Comprehension to scope out the range, and check if the seed is within the range.
#   - < > operators instead of spelling out the entire range.
#   - Too high