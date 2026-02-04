#3
largest = None
smallest = None
while True:
    try:
        number = input('Please input a number, press Enter to stop: ')
        if number == "":
            print('largest number:', largest)
            print('smallest number:', smallest)
            break
        s = float(number)
        if largest is None:
            largest = s
            smallest = s
        else:
            if s > largest:
                largest = s
            if s < smallest:
                smallest = s
    except:
        print('Please enter number')



