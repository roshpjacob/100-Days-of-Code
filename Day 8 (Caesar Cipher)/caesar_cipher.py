# Cipher Encryption
def encrypt(text1, shift1):
    cipher = ""
    for i in text1:
        if i.isalpha():
            n = ord(i) + shift1
            if n > 122:
                n = n - 122
                n = 96 + n
            cipher += chr(n)
        else:
            cipher += i

    print("Encoded Message is: ", cipher)


# Cipher Decryption
def decrypt(txt, sft):
    decipher = ""
    for i in txt:
        n = ord(i) - shift
        if n < 97:
            n = 97 - n
            n = 123 - n

        decipher += chr(n)

    print("Decoded message is: ", decipher)
