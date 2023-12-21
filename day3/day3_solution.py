# could have added leading and trailing periods to avoid edge cases.... oh well
# PART 1
# first find out what special symbols are there in the document
SYMBOLS = ""
with open("./day3/input.txt", "r") as file:
    # remove leading and trailing spaces (e.g. from new line)
    file_lines = list(map(lambda x: x.strip(), file.readlines()))
    LINE_LENGTH = len(file_lines[0])
    N_LINES = len(file_lines)
    # print(N_LINES)
    # print(LINE_LENGTH)
    for line in file_lines:
        for char in line:
            # print(char)
            if char != "." and char != "\n" and char.isnumeric() is False and not char in SYMBOLS:
                SYMBOLS += char

    print(SYMBOLS)

    sum = 0

    for line_index in range(N_LINES):
        this_line = file_lines[line_index]
        # previous and next lines
        if line_index == 0:
            # print(f"line length check: {LINE_LENGTH}")
            prev_line = "".join(["." for i in range(LINE_LENGTH)])
            next_line = file_lines[line_index + 1]
        elif line_index == N_LINES - 1:
            prev_line = file_lines[line_index - 1]
            next_line = "".join(["." for i in range(LINE_LENGTH)])
        else:
            prev_line = file_lines[line_index - 1]
            next_line = file_lines[line_index + 1]

        line_numbers = []
        line_numbers_positions = []

        for char_index in range(LINE_LENGTH):
            this_char = this_line[char_index]
            if char_index == 0:
                prev_char = "."
                next_char = this_line[char_index + 1]
            elif char_index == LINE_LENGTH - 1:
                prev_char = this_line[char_index - 1]
                next_char = "."
            else:
                prev_char = this_line[char_index - 1]
                next_char = this_line[char_index + 1]

            # get all the numbers from this line
            if this_char.isnumeric() is False:
                if prev_char.isnumeric() is True:
                    # if previous is numeric and this char is non-numeric,
                    # last char is the end of number, add number to list
                    line_numbers.append(current_num)
                    # end index of number
                    number_end = char_index - 1
                    # add start and end index to list
                    line_numbers_positions.append([number_start, number_end])
                elif prev_char.isnumeric() is False:
                    # if previous is non-numeric and current char is non-numeric, move on
                    pass
            elif this_char.isnumeric() is True:
                # if this is the last character, need to check edge case number
                if char_index == LINE_LENGTH - 1:
                    # if prev char is not numeric, start new number and add to list
                    if prev_char.isnumeric() is False:
                        current_num = this_char
                        line_numbers.append(current_num)
                        # this is a single digit number, so start and end index are the same
                        number_start = number_end = char_index
                        line_numbers_positions.append(
                            [number_start, number_end])
                    # if prev char is numeric, update number and add to list
                    elif prev_char.isnumeric() is True:
                        current_num += this_char
                        line_numbers.append(current_num)
                        # this is the end of number
                        number_end = char_index
                        line_numbers_positions.append(
                            [number_start, number_end])
                # if this is not the last character
                else:
                    if prev_char.isnumeric() is True:
                        # if prev char is numeric and this char is numeric, update number
                        current_num += this_char
                    elif prev_char.isnumeric() is False:
                        # if prev char is non-numeric and this char is numeric, start new number
                        current_num = this_char
                        # this is the start of number
                        number_start = char_index

        print(line_numbers)
        print(line_numbers_positions)

        # we now have the numbers and their start and end indices for the current line
        # now we can check if adjacent characters are special symbols
        for i in range(len(line_numbers)):
            this_num = int(line_numbers[i])
            num_start_index = line_numbers_positions[i][0]
            num_end_index = line_numbers_positions[i][1]
            # get all adjacent characters
            adj_chars = ""

            # if it is a well behaved middle number
            if num_start_index != 0 and num_end_index != LINE_LENGTH - 1:
                # adjacent chars from previous line and next line
                for char_index in range(num_start_index-1, num_end_index + 2):
                    adj_chars += prev_line[char_index]
                    adj_chars += next_line[char_index]
                # adjacent chars from current line
                adj_chars += this_line[num_start_index - 1]
                adj_chars += this_line[num_end_index + 1]
            # starting edge number
            elif num_start_index == 0:
                for char_index in range(num_start_index, num_end_index + 2):
                    adj_chars += prev_line[char_index]
                    adj_chars += next_line[char_index]
                adj_chars += this_line[num_end_index + 1]
            # ending edge number
            elif num_end_index == LINE_LENGTH - 1:
                for char_index in range(num_start_index - 1, num_end_index + 1):
                    adj_chars += prev_line[char_index]
                    adj_chars += next_line[char_index]
                adj_chars += this_line[num_start_index - 1]

            # check if this number's adjacent chars include special symbols
            special = False
            for symbol in SYMBOLS:
                if symbol in adj_chars:
                    special = True
            if special is True:
                sum += this_num
    print(sum)
