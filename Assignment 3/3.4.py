import random
number = random.randint(1, 10)
while True:
    try:
        a = float(input('guess a number?:'))
        if a == number:
            print('correct')
            break
        elif a > number:
            print("too high")
        else:
            print("too low")
    except:
        print("please input a number")
