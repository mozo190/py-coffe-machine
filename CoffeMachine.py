MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
is_on = True


def calculate():
    global profit
    if total < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(total - drink_cost, 2)
        profit += drink_cost
        print(f"Here is ${change} in change.")
        resources["water"] -= water
        resources["coffee"] -= coffee
        resources["milk"] -= milk
        print(f"Here is your {user_input} ☕️. Enjoy!")
    return profit


while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        drink_ingredients = drink["ingredients"]
        drink_cost = drink["cost"]
        water = drink_ingredients["water"]
        coffee = drink_ingredients["coffee"]
        milk = 0
        if "milk" in drink_ingredients:
            milk = drink_ingredients["milk"]
        if resources["water"] < water:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < coffee:
            print("Sorry there is not enough coffee.")
        elif resources["milk"] < milk:
            print("Sorry there is not enough milk.")
        else:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            profit = calculate()

# Path: CoffeMachine.py

