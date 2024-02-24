import random
from art import logo
import os

"""
Here are some basic rules for a game of blackjack:
-> Jack, King and Queen have a value of 10
-> Cards you are dealing should not add up to a value more than 21.
If it does, its called a bust and you lose, irregardless of how much the margin from 21 is.
-> The Ace card can take the value of 1 or 11 according to the player's requirement to get near the value of 21.
-> If the dealer has a value less than 17, then dealer must draw another card.
"""


def deal_card():
    """Draws a random card from the deck of Unique cards with replacement(assume)"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """To calculate the total value in hand"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user, comp):
    """Compares the scores and evaluates the final result"""
    user = calculate_score(user)
    comp = calculate_score(comp)

    if user > 21 and comp > 21:
        return "It's a bust. You went over and lost. Try again."
    elif user == comp:
        return "DRAW"
    elif user > 21:
        return "BUST. You lose. Try again"
    elif comp > 21:
        return "Dealer loses"
    elif user == 0:
        return "BLACKJACK! You Win!"
    elif comp == 0:
        return "You lose. Dealer has a BLACKJACK!"
    elif user > comp:
        return "You WIN!"
    else:
        return "You lose"


def play():
    """Main Function to execute the playable part"""
    print(logo)

    user_cards = []
    computer = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer)
        print(f"    Cards in Hand: {user_cards}     Current score: {user_score}")
        print(f"    Computer's Cards: [{computer[0]}, ?]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            deal = input("Type 'y' to deal another card or type 'n' to pass")
            if deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(f"    Your Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"    Computer's Final Hand: {computer}, Final Score: {computer_score}")
    print(compare(user_cards, computer))


while input("Do you want to play a game of BlackJack? Type 'y' for yes and 'n' for no: ") == "y":
    os.system('cls')
    play()
