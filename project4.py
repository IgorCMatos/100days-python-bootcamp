import random

player = int(input("Choose: 0 - Rock, 1 - Paper or 2 - Scissors: "))
computer = random.randint(0, 2)

if player < 3:
    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It is a TIE")
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("You win")
    else:
        print("You lost")
else:
    print("Invalid number")
