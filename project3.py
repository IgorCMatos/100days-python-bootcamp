print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
first_choice = input("Left or Right?").strip().lower()
if first_choice == "right":
    print("Game over")
elif first_choice == "left":
    second_choice = input("Swim or Wait?").strip().lower()
    if second_choice == "swim":
        print("Game over")
    elif second_choice == "wait":
        last_choice = input("Which door? Red, Blue or Yellow").strip().lower()
        if last_choice == "red":
            print("Game over")
        elif last_choice == "blue":
            print("Game over")
        elif last_choice == "yellow":
            print("You Win!")
        else:
            print("Not a valid option!")
    else:
        print("Not a valid option!")
else:
    print("Not a valid option!")
