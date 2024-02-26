class Coffee:
    def __init__(self):
        self.resources = {
            "water": 2000,
            "coffee": 300,
            "milk": 1000
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Milk: {self.resources['milk']}ml")

    def sufficiency(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Not enough {item}. Please report immediately to restock.")
                return False

        return True

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

