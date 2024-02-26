class Finance:
    coin_values = {
        "quarters": 0.25,
        "dimes": 0.1,
        "pennies": 0.01,
        "nickles": 0.05
    }

    def __init__(self):
        self.money_received = 0
        self.profit = 0

    def report(self):
        """Prints the total sales during on state"""
        print(f"Net Sales: ${self.profit}")

    def process_coins(self):
        for i in self.coin_values:
            self.money_received += int(input(f"How many {i} inserted: ")) * self.coin_values[i]

        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Processing change of ${change}")
            self.profit += cost
            self.money_received = 0
            return True

        else:
            print("Insufficient funds. Refund initiated.")
            return False

    
