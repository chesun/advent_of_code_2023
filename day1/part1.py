# Day 1 of the advent of code: finding calibration values from file
with open("./day1/input.txt", "r") as rawfile:
    lines = rawfile.readlines()
    calib_val = 0
    for line in lines:
        # initialize a list for numeric characters in the line
        num_chars = []
        for char in line:
            if char.isnumeric() is True:
                num_chars.append(char)
        if len(num_chars) == 2:
            line_val = int("".join(num_chars))
        elif len(num_chars) == 1:
            line_val = int(num_chars[0] + num_chars[0])
        elif len(num_chars) > 2:
            line_val = int(num_chars[0] + num_chars[-1])
        else:
            raise ValueError
        calib_val += line_val
    print(calib_val)