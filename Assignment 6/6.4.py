def word(text):
    words = text.split()
    f = {}
    for w in words:
        if w in f:
            f[w] += 1
        else:
            f[w] = 1
    return f
text = input("Enter text: ")
result = word(text)
for word in result:
    print(word, ":", result[word])

