def hightest_value(bid_dictionary):
    winner = ""
    highets_bid = 0

    for person in bid_dictionary:
        bid_amount = bid_dictionary[person]

        if bid_amount > highets_bid:
            highets_bid = bid_amount
            winner = person

    print(f"The winner is {winner} with a bid of ${highets_bid}.")


bid = {}

more_people = True

while more_people == True:
    name = input("Whats is your name? \n")
    price = int(input("What is your bid? \n"))
    bid[name] = price

    continue_bid = input(
        "Is there more people to bid? 'yes or 'no' \n").lower().strip()

    if continue_bid == "no":
        more_people = False
        hightest_value(bid)
    elif continue_bid == "yes":
        print("\n" * 100)
