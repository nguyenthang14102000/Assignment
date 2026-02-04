#2
while True:
    try:
        a = float(input('inch (input negative number to end):'))
        if a>=0:
            a = a*2.54
            print('cm',a)
        else:
            break
    except:
        print('Please input a number')

