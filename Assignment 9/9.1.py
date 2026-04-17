def count_lines(filename):
    count = 0
    file = open(filename, "r")
    for line in file:
        if line.strip() != "":
            count += 1
    file.close()
    return count