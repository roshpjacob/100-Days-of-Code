print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
split = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give?"))

total += total*tip_percentage/100
tip = round(total/split, 2)

print(f"Each person should pay: ${tip}")
