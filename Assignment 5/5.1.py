n = []
while True:
    number = input("PLease press 'enter' to end: ")
    if number == "":
        break
    else:
        try:
            number = float(number)
            n.append(number)
        except:
            print("PLease enter number")
n.sort(reverse=True)
print(n[:5])
