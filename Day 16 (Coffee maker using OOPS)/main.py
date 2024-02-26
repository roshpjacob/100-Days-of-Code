from coffee_maker import Coffee
from finance import Finance
from menu import Menu, MenuItem

menu = Menu()
finance = Finance()
coffee_maker = Coffee()

is_on = True
coffee_maker.report()
finance.report()


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have? {options}")
    if choice == "off":
        is_on = False
        print("Power Off")
    elif choice == "report":
        coffee_maker.report()
        finance.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.sufficiency(drink) and finance.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print(f"Here is your rejuvenating cup of {choice}. Thank you come again!")





