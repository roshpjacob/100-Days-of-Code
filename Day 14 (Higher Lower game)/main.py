import os
from art import logo, vs
from data import data
import random


# Format account data into printable and user readable form
def format_data(account):
    """Takes account data from data.py and returns a printable format"""
    acc_name = account["name"]
    acc_descr = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_descr}, from {acc_country}"


def check_guess(guess, fola, folb):
    """Compares the followers of A and B and checks user's guess"""
    if fola > folb:
        return guess == 'a'
    else:
        return guess == 'b'
    # The above if-else statement is a easier way of saying, if A has more followers than B,
    # and if guess is 'A' then return true else if b has more followers and guess is 'B', then return, else no returns


# Printing art
print(logo)
score = 0
game = True
acc_a = random.choice(data)

while game:

    acc_b = random.choice(data)
    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A: {format_data(acc_a)}.")
    print(vs)
    print(f"Against B: {format_data(acc_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Choose A or B:  ").lower()

    # Checking if user guessed right using follower counts
    a_followers = acc_a["follower_count"]
    b_followers = acc_b["follower_count"]
    is_correct = check_guess(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You guessed right! Current score: {score}")
        acc_a = acc_b
    else:
        game = False
        print(f"You guessed wrong :(\nFinal Score: {score}")
