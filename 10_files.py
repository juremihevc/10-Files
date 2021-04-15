with open("ninja.txt", "r+") as ninja_file:
    lines_list = ninja_file.read().splitlines()
    next_list = "to je nova"
    lines_list.append(next_line)

    ninja_file.write(line_list)