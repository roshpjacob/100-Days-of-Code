from caesar_cipher import encrypt
from caesar_cipher import decrypt


choice = "Yes"
while choice == "Yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)

    elif direction == "decode":
        decrypt(text, shift)

    choice = input("Do you want to try for another message? (Yes or No)")

print("\nThank you, come again!")

