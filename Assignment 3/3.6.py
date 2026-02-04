def fe():
    c = input("Write:")
    b = len(c)
    print(b)
    if b % 2 == 0:
        a = c[(b // 2) - 1:(b // 2) + 1]
        print(a)
    else:
        a = c[b // 2]
        print(a)
fe()



