Menu = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffe": 18,

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffe": 24,
        },
        "cost": 2.5,
    },
    "expresso": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffe": 24,
        },
        "cost": 3.0,
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, thre is not enough{item}.")
            return False
    return True


def coin():
    print("Insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transcation(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


Machine_working = True

while Machine_working:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        Machine_working = False
    elif choice == "report":
        for resource, amount in resources.items():
            print(f"{resource}: {amount}")
    else:
        drink = Menu[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = coin()
            if transcation(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])
