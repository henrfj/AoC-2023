"""
While you wait for the ferry, maybe you can help us with our food production problem. 
The latest Island Island Almanac just arrived and we're having trouble making sense of it.

seeds to be planted +
soil -> Seeds
Fertilizer -> soil
water -> fertilizer
...
numbers are NOT IDs and are reused for each category.


source-to-destination map:
destination range start source range start range

seed-to-soil map:
50 98 2
=> | soil 50, 51 | seed 98 and 99 | 
=> soil 50 <-> seed 98 | soil 51 <-> seed 99

NB!
Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

"""

def seedy(seed_mapps : list[list]) -> int:
    #
    seeds = seed_mapps[0].split(": ")[-1].strip().split(" ")
    seeds = [int(s) for s in seeds]
    #seed_dict = {}
    #for i, s in enumerate(seeds):
    #    seed_dict[i] = [s]
    #
    src_ranges = []
    dst_ranges = []
    for line in seed_mapps[3:]:
        if ""==line or "end"==line:
            # TODO logic to look inside ranges
            for i, seed in enumerate(seeds): #SRC
                #
                for idx, (start, stop) in enumerate(src_ranges):
                    if start <= seed < stop:
                        dist_from_start = seed-start

                        seeds[i] = dst_ranges[idx][0] + dist_from_start
                        break  
                #seed_dict[i].append(seeds[i])

            src_ranges = []
            dst_ranges = []

        elif "-to-" in line:
            continue
        else:
            l = line.split(" ")
            # Extract useful info
            dst_start = int(l[0])
            src_start = int(l[1])
            range_ = int(l[2])
            #
            src_ranges.append((src_start, src_start+range_))
            dst_ranges.append((dst_start, dst_start+range_))

    #print(seed_dict)
    return min(seeds)

with open('test_input.txt', 'r') as f:
    seed_mapps = [line.strip() for line in f]

with open('input.txt', 'r') as f:
    seed_mapps = [line.strip() for line in f]




location = seedy(seed_mapps)

print(location)

# TODO
#   - New method: just follow the seeds through the layers - dont produce a "full map first"
#   - Use List Comprehension to scope out the range, and check if the seed is within the range.
#   - < > operators instead of spelling out the entire range.
#   - Too high