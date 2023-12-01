"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
 one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

"""
"""
BUG:
- a string number can be a part of another: eightwothree => 8, 2, 3
- EZ fix, keep last letter when "resetting"
"""

# Open the file in read mode
file = open('input.txt', 'r')
test_file = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
"asdasdsadthreeasdasdasd"]

string_numbers = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}


# Loop through each line in the file
s = 0
for line in file:
    numbs = {}
    expanding_string = ""
    for idx, l in enumerate(line):
        # First, check for actual numeral
        try:
            n = int(l)
            numbs[idx] = n
            expanding_string = "" # Reset
        # If not, take a look at expanding string
        except ValueError:
            expanding_string += l
            for string_number in string_numbers.keys():
                # NOTE: this indexing could be wrong...
                if string_number in expanding_string:
                    numbs[idx] = string_numbers[string_number]
                    expanding_string = expanding_string[-1] # Almost reset # BUG FIX?
                    break # The inner for-loop

    # Unwrap the dictionary
    sorted_indexes = sorted(numbs.keys())
    first = str(numbs[sorted_indexes[0]])
    last = str(numbs[sorted_indexes[-1]])
    #
    a = int(first+last)
    s += a

    print(numbs, a, s)
    
    


#print(s)
file.close()