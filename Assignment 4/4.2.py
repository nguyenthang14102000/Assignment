while True:
    n = input("Please enter color code: ")
    code = list(n)
    if len(code) == 7:
        if code[0] != "#":
            print("Wrong")
        else:
            for i in range(1, 7):
                c = code[i]
                if c.isdigit() or c.upper() in "ABCDEF":
                    if i == 6:
                        print("True")
                        break
                else:
                    print("Wrong")
            else:
                continue
            if i == 6 and c.isdigit() or c.upper() in "ABCDEF":
                break
    else:
        print("Wrong")