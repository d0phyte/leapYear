
year = int(input("Which year do you want to check? Leap years have 366 days, with an extra day in February: "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 != 0: 
        print("This is not a leap year.")
    else:
        print("This a leap year.")

elif year % 4 == 0 and year % 100 != 0:
    print("This a leap year.")


else:
    print("This is not a leap year.")