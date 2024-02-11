import random

names_string = input("Enter the names of everyone present: ")
names = names_string.split(", ")
random_no = random.randint(0, len(names)-1)
print(names)
print(names[random_no], "should pay the bill")
