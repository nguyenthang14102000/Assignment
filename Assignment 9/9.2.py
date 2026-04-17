def find_keyword(filename, keyword):
    lines_found = []
    file = open(filename, "r")
    line_number = 1
    for line in file:
        if keyword in line:
            lines_found.append(line_number)
        line_number += 1
    file.close()
    return lines_found