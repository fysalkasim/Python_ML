year = int(input("Enter the year you wish to calculate : "))
if year % 4 != 0:
    print("It is not a leap year")
elif year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")

