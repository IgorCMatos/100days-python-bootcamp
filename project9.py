def add(first_value, second_value):
    return first_value + second_value


def subtract(first_value, second_value):
    return first_value - second_value


def multiply(first_value, second_value):
    return first_value * second_value


def divide(first_value, second_value):
    if second_value == 0:
        return "Error! Division by zero."
    return first_value / second_value


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    more_numbers = True
    print("Python Calculator")
    first_value = float(input("First number: "))

    while more_numbers:

        symbol = input("Type the equation symbol \n +\n -\n /\n *\n")

        if symbol not in operation:
            print("Invalid operation symbol! Please try again.")
            continue

        second_value = float(input("Second number: "))

        result = operation[symbol](first_value, second_value)
        print(f"{first_value} {symbol} {second_value} = {result}")

        restart = input(
            f"Type 'yes' to continue calculation with {result}, or type 'no' to start a new calculation or 'exit' to leave: ")
        if restart == "yes":
            first_value = result
        elif restart == "no":
            more_numbers = False
            calculator()
        elif restart == "exit":
            break


calculator()
