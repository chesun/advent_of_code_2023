##########################################################################
# part 1
##########################################################################
# solve this by splitting each line
all_colors = ["red", "green", "blue"]
bag = {"red": 12, "green": 13, "blue": 14}
sum_possible_ids = 0
sum_power = 0

with open("./day2/input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        #######################################
        # get game id
        #######################################
        game_str = line.split(":")[0]
        game_id_str = ""
        for char in game_str:
            if char.isnumeric() is True:
                game_id_str += char
        # integer for game id
        game_id = int(game_id_str)
        game_possible = True

        #######################################
        # get different rounds 
        #######################################
        rounds_str = line.split(":")[1].strip()
        rounds = rounds_str.split(";")

        # a list to hold all rounds as strings
        rounds_cleaned = []

        # list of values for the number of cubes for each color
        color_numbers = {color : [] for color in all_colors}
        # looping over rounds in the current game
        for round_str in rounds:
            # list for the round
            round = round_str.split(",")
            # strip leading and trailing spaces
            for index in range(len(round)):
                round[index] = round[index].strip()
            # make a dictionary for the round
            colors = [str.split()[1] for str in round]
            numbers = [int(str.split()[0] )for str in round]
            # dictionary for the round
            round_dict = {color : number for color, number in zip(colors, numbers)}
            
            # complete the round dictionary by adding 0 to nonexisting colors
            for color in all_colors:
                if color not in round_dict.keys():
                    round_dict[color] = 0
            # print(round_dict)
            # check if this round is possible
            for color in all_colors:
                color_numbers[color].append(round_dict[color])
                if round_dict[color] > bag[color]:
                    game_possible = False
        # print(color_numbers)
        # calculate the power of the minimum possible numbers
        power_game = max(color_numbers["red"]) * max(color_numbers["green"]) * max(color_numbers["blue"])
        sum_power += power_game

        if game_possible is True:
            sum_possible_ids += game_id

    print(sum_possible_ids, sum_power)




            

                    


