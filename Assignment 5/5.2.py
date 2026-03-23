while True:
    try:
        number = int(input("Please enter a number: "))
        S = 0
        for i in range(1,int(number**0.5)+1):
            if number % i == 0:
                S += 1
        if S > 1:
            print(f"{number} is not a prime number.")
            break
        else:
            print(f"{number} is a prime number.")
            break
    except:
            print("Please enter a number")



