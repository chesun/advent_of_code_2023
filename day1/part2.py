# part 2 of day 1: need to take into account numbers spelled with letters
# need to deal with multiple occurences of one string, .find() only returns index of first occurence

import re 
import itertools

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
           "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers_numeric = ["1", "2", "3", "4", "5", "6", "7", "8", "9", 
                   "1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_dict = dict(zip(numbers, numbers_numeric))

with open("./day1/input.txt", "r") as file:
    textlines = file.readlines()
    calib_val = 0
    for line in textlines:
        line_numbers_index = {}
        # check if there are any number 
        for number in numbers:
            if line.find(number) != -1: # this word exists
                lowest_index = line.find(number)
                highest_index = line.rfind(number)
                line_numbers_index[number] = [lowest_index, highest_index] # smallest and highest index of substring
        # how many number there are in line
        n_numbers = len(line_numbers_index)
        if n_numbers == 1:
            line_val = int(number_dict[list(line_numbers_index.keys())[0]] + number_dict[list(line_numbers_index.keys())[0]])
            # print(line_numbers_index)
        elif n_numbers >= 2:
            # find the overall min and max index
            min_index = min([i[0] for i in line_numbers_index.values()])
            # print(min_index)
            max_index = max([i[1] for i in line_numbers_index.values()])
            # print(max_index)
            # find the key for the min and max index
            for number, indices in line_numbers_index.items():
                if min_index in indices:
                    digit1 = number_dict[number]
                if max_index in indices:
                    digit2 = number_dict[number]
            line_val = int(digit1 + digit2)

        print(line_val)
        calib_val += line_val
    print(calib_val)

