def make_uppercase(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()
    text = text.upper()
    out = open("output.txt", "w")
    out.write(text)
    out.close()