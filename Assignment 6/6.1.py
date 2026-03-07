n = []
while True:
    number = input("nhap so :")
    if number == "":
        break
    else:
        n.append(float(number))
n.sort(reverse=True)
print("Top 5 greatest numbers:")
print(n[:5])
