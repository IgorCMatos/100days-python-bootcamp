import random


def set_life(difficult):
    global total_life
    if difficult == 'easy':
        total_life = 20
    elif difficult == 'hard':
        total_life = 5


def check_answer(player_guess):
    global total_life

    if player_guess < random_number:
        print("Guess Higher")
        total_life -= 1

    elif player_guess > random_number:
        print("Guess Lower")
        total_life -= 1

    elif player_guess == random_number:
        print(f"You won!!! The number was {random_number}")
        return True

    return False


random_number = random.choice(range(1, 101))
print(random_number)
print("Guess the number")
difficult = input("Set your dificulty level 'easy' or 'hard' \n").lower()

total_life = -1
set_life(difficult)

while total_life > 0:
    print(f"You have {total_life} lives remaining.")
    player_guess = int(input("Your guess: "))
    if check_answer(player_guess):
        break
    if total_life == 0:
        print(f"Game over! The number was {random_number}.")
