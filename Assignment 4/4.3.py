def total():
    m = input("Please enter a paragraph:")
    u = list(m)
    numbers = []
    a = ""
    for i in u:
        if i.isdigit():
            a += i
        elif a != "":
            numbers.append(int(a))
            a = ""
    if a != "":
        numbers.append(int(a))
    print("Sum =", (sum(numbers)))
total()