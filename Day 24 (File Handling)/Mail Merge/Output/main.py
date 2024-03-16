f = open("./Input/Letters/starting_letter.txt", "r")
letter_body = f.read()
f.close()

f = open("./Input/Names/invited_names.txt", "r")
filename = "letter_for_name.txt"

for i in f:
    name = i
    name = name.strip("\n")
    x = filename
    file = letter_body
    x = x.replace("name", name)
    file = file.replace("[name]", name)
    g = open(f"./Output/ReadyToSend/{x}", "w")
    g.write(file)
    g.close()
