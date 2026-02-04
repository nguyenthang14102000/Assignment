def acros():
    a = input('Write your words:')
    b = a.split()
    n = ""
    for f in b:
        n = n + f[0]
    return n
m = acros()
print(m.upper())


