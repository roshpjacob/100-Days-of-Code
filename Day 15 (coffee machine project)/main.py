MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

stats = 0
resources = {
    "water": 6000,
    "milk": 2000,
    "coffee": 300,
}


# Check resources for order
def is_resource(order):
    """A function to check if resources are available for requested order"""
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {order[item]}. Kindly raise a request for resources.")
            return False

    return True


def process_coins():
    """A function to process coins into Dollars"""
    print("Please insert coins")
    total = int(input("Insert quarters: ")) * 0.25
    total += int(input("Insert dimes: ")) * 0.1
    total += int(input("Insert nickles: ")) * 0.05
    total += int(input("Insert pennies: ")) * 0.01
    return total


def transaction_success(paid, payable):
    if payable <= paid:
        change = round(paid - payable, 2)
        print(f"Here is ${change} in change.")
        global stats
        stats += payable
        return True
    else:
        print("Not enough money! Refund Initiated.")
        return False


def make_coffee(order, order_ing):
    for item in order_ing:
        resources[item] -= order[item]



is_on = True

while is_on:
    print("Welcome to Papi's Kaapi\n\n")
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Collection : ${stats}")
    else:
        drink = MENU[choice]
        if is_resource(drink['ingredients']):
            payment = process_coins()
            if transaction_success(payment, drink['cost']):
                make_coffee(drink['ingredients'], list(drink['ingredients'].keys()))
                print(f"Here is your order, one {choice}. Enjoy! Come Again!")
