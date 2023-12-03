##########################################################################
# part 1
##########################################################################
# solve this by splitting each line
all_colors = ["red", "green", "blue"]
bag = {"red": 12, "green": 13, "blue": 14}
sum_possible_ids = 0

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

        # convert each round into a dictionary
        rounds_cleaned = []
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
                if round_dict[color] > bag[color]:
                    game_possible = False
        
        
        if game_possible is True:
            sum_possible_ids += game_id

          

        

    print(sum_possible_ids)




            

                    


