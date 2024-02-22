def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    choice = "yes"
    p = float(input("Enter first number: "))

    while choice == "yes":
        q = float(input("Enter second number: "))
        oprn = input("Enter required operation: ")

        answer = operation[oprn](p, q)
        print(f"{p} {oprn} {q} = {answer}")
        choice = input("Do you want to perform another operation using the answer? Type 'yes' if needed, or 'no' if "
                       "you want to perform a new calculation.\n Enter any other key to exit. ")
        if choice == "yes":
            p = answer

        elif choice == "no":
            calculator()

        else:
            quit()


calculator()
