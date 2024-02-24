import random


def guess_number():
    """This is where the game begins"""
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 to 100.")
    choice = input("Choose a difficulty ('easy' or 'hard') : ")

    if choice == "hard":
        chance = 5
        rand = random.randint(1, 100)

    elif choice == "easy":
        chance = 10
        rand = random.randint(1, 100)

    else:
        print("INVALID CHOICE")
        quit()

    while chance > 0:
        print(f"You have {chance} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > rand:
            print("Too High. Think low and guess again.")
            chance -= 1
        elif guess == rand:
            print("YOU GUESSED RIGHT!")
            break

        else:
            print("Too Low. Think high and guess again.")
            chance -= 1

    if chance == 0:
        print("Chances Exhausted :(")
    if input("Do you want to try again? ") == 'y':
        guess_number()
    else:
        quit()


guess_number()
