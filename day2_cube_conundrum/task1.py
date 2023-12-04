"""
Bag of cubes: green, red or blue. 
Grab a handful, then put back in the bag. 
Game N: n blue, k red, m green; .... ; ....; ....
- If there are no blue: "k red, m green;"


1: The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?


"""



test_file = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
"Game 10: 1 green; 16 green, 3 red, 2 blue; 1 blue, 16 green, 4 red; 16 green, 5 red, 2 blue"]


# Open the file in read mode
file = open('input.txt', 'r')

#
max_dict = {"red" : 12, "blue" : 14, "green" : 13}
#
s = 0
# Loop through each line in the file
for game in file: # One Game
    game = game.strip()
    #
    game = game.split(":")
    game_no = int(game[0].split(" ")[-1])
    #print(game_no, end=": ")
    #
    game = game[1:][0].split(";")
    #
    good_flag = True
    for draw in game: # One draw
        draw = draw.split(", ")
        for d in draw:
            d = d.strip().split(" ")
            num = int(d[0])
            color = d[1]
            if num > max_dict[color]:
                good_flag = False
                #print(color, num, end=" | ")
    if good_flag:
        s += game_no
    #    print(" s=", s)
    #else:
    #    print()

print(s)

##############################################
