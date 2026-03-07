while True:
    try:
        seasons = ("winter", "spring", "summer", "autumn")
        month = int(input("Enter month number (1-12): "))
        if month < 1 or month > 12:
            print("Please enter a valid month number")
        else:
            i = (month % 12) // 3
            print(seasons[i])
            break
    except:
        print("Please enter a valid month number")