def phone():
    m = input("document: ")
    u = list(m)
    l = ""
    k = ""
    for i in u:
        if i == "+" or i.isdigit():
            k += i
        else:
            if k != "" and (len(k) == 10 or k[:3] == "+84"):
                l += "[REDACTED]"
            else:
                l += k
            l += i
            k = ""
    if k != "":
        if len(k) == 10 or k[:3] == "+84":
            l += "[REDACTED]"
        else:
            l += k
    print(l)
phone()

