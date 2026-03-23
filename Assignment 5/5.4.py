def s(number):
    total = 0
    for n in number:
        total += n
    return total

#testing
n = [1,2,3,4,5,6,7,8,9]
re = s(n)
print("Sum of the list:", re)

