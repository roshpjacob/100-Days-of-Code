import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

comp = [rock, paper, scissors]
a = "Yes"
while a == "Yes":
    play = random.randint(0, 2)
    user = int(input("What do you want to play? Type 0 for Rock, 1 for Paper, 2 for Scissors)"))

    if user == 0 and play == 1:
        print("You chose: ", comp[user], "\n I chose: ", comp[play],
              "\n\nI WIN! Better luck next time. Try again? (Yes or No)")
        a = input()

    elif user == 1 and play == 2:
        print("You chose: ", comp[user], "\n I chose: ", comp[play],
              "\n\nI WIN! Better luck next time. Try again? (Yes or No)")
        a = input()

    elif user == 2 and play == 0:
        print("You chose: ", comp[user], "\n I chose: ", comp[play],
              "\n\nI WIN! Better luck next time. Try again? (Yes or No)")
        a = input()

    elif user == play:
        print("You chose: ", comp[user], "\n I chose: ", comp[play],
              "\n\nIt's a DRAW! Try again? (Yes or No)")
        a = input()

    else:
        print("You chose: ", comp[user], "\n I chose: ", comp[play], "\n\nYou Win! Womp Womp. "
                                                                     "Won't happen next time. Try again? (Yes or No)")
        a = input()

