from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_machine = CoffeeMaker()
coffee_menu = Menu()
money_tracker = MoneyMachine()

while True:
  user_choice = input(f"What would you like? (espresso/ latte/ cappuccino): ").lower()
  if user_choice == "report":
    coffee_maker_machine.report()
    money_tracker.report()
  elif user_choice == "off":
    break
  else: 
    drink = coffee_menu.find_drink(user_choice)
    if drink:
      if coffee_maker_machine.is_resource_sufficient(drink):
        if money_tracker.make_payment(drink.cost):
          coffee_maker_machine.make_coffee(drink)