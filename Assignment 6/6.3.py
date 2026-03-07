n = []
while True:
    name = input("Your name :")
    if name == "":
        break
    else:

        if name in n:
            print("Existing name")
        else:
            print("New name")
            n.append(name)
for i in n:
    print(i)

