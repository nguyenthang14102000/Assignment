def m(a):
    n = []
    for i in a:
        if i % 2 == 0:
            n.append(i)
    return n
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = m(numbers)
print("Original list:", numbers)
print("Without odd numbers:", result)