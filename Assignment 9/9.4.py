def average_score(filename):
    file = open(filename, "r")
    total = 0
    count = 0
    for line in file:
        data = line.strip().split(",")
        score = int(data[1])

        total = total + score
        count = count + 1
    file.close()
    average = total / count
    return average