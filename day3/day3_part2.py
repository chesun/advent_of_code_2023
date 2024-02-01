''' day 3 part 2'''


def find_symbols(input_file):
    '''Find special symbols and all symbols in the input file'''
    with open(input_file, "r", encoding="utf-8") as file:
        special_symbols = []
        all_symbols = []
        for line in file.readlines():
            for char in line:
                if not char.isnumeric() and not char in all_symbols:
                    all_symbols += char
                if (char != "."
                    and char != "\n"
                    and not char.isnumeric()
                        and not char in special_symbols):
                    special_symbols += char
    # print("special symbols: ", special_symbols)
    # print("all symbols: ", all_symbols)
    return special_symbols, all_symbols


def max_num_len(input_file, all_symbols_list):
    '''Find maximum length of numbers in input file'''
    with open(input_file, "r", encoding="utf-8") as file:
        max_len = 0
        for line in file.readlines():
            print("iterating over first line")
            replaced_line = line
            # replace all symbols with white space
            for symbol in all_symbols_list:
                replaced_line = replaced_line.replace(symbol, " ")
            # split line into list
            split_elements = replaced_line.split(" ")
            print("split elements: ", split_elements)
            # find the lengths of numbers in this line
            line_num_lengths = list(map(len, split_elements))
            max_len_line = max(line_num_lengths)
            if max_len_line > max_len:
                max_len = max_len_line
    print("max length of number is ", max_len)
    return max_len


def main(file_path):
    '''Main function to solve day 3 part 2'''
    print(find_symbols(file_path))
    max_num_len(file_path, find_symbols(file_path)[1])


if __name__ == "__main__":
    main("day3/input.txt")
