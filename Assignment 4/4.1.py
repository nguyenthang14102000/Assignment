n = input("Please enter your course: ")
code = list(n)
if len(code) == 6:
    if code[0].isupper() and code[1].isupper() and code[2].isupper() \
       and code[3].isdigit() and code[4].isdigit() and code[5].isdigit():
        print("True")
    else:
        print("Wrong")
else:
    print("Wrong")