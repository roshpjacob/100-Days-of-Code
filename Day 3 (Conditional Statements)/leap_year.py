# A year is said to be a leap year, if it is divisible by 4.
# But if it is also divisible by 100, then it should also be divisible by 400, else it is not leap

choice = "yes"
while choice == "yes":

    year = int(input("Enter the year to be checked: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")

            else:
                print("Not a leap year")

        else:
            print(f"{year} is a leap year")

    else:
        print(f"{year} is not a leap year")

    choice = input("\nDo you want to check for another year?(yes or no) ")
    choice = choice.lower()

print("Run me again to check other years")
