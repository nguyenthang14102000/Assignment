def env(s):
    n = []
    for i in s:
        if i % 2 == 0:
            n.append(i)
    return n

#testing
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
re = env(m)
print("Original list:", m)
print("Even numbers:", re)
