"""
Bag of cubes: green, red or blue. 
Grab a handful, then put back in the bag. 
Game N: n blue, k red, m green; .... ; ....; ....
- If there are no blue: "k red, m green;"


2: what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

"""



test_file = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]


# Open the file in read mode
file = open('input.txt', 'r')


#
s = 0
# Loop through each line in the file
for game in file: # One Game
    #
    max_dict = {"red" : 0, "blue" : 0, "green" : 0}
    #
    game = game.strip()
    #
    game = game.split(":")
    game_no = int(game[0].split(" ")[-1])
    #print(game_no, end=": ")
    #
    game = game[1:][0].split(";")
    #
    for draw in game: # One draw
        draw = draw.split(", ")
        for d in draw:
            d = d.strip().split(" ")
            num = int(d[0])
            color = d[1]
            if num > max_dict[color]:
                max_dict[color] = num
    #
    power = 1
    for k in max_dict.keys():
        power *= max_dict[k]
    print(power)
    s += power
print(s)

##############################################
file.close()