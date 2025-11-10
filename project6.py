import random

words = ["cat", "dog", "banana", "apple", "car",
         "fish", "orange", "parrot", "grape", "book"]

random_word = random.choice(words)
hidden_word = ['_'] * len(random_word)

attempts = 10
while attempts > 0 and '_' in hidden_word:
    player_guess = input("Type a letter: ").lower()

    if player_guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == player_guess:
                hidden_word[i] = player_guess
        print("Ok! The word now is: " + ' '.join(hidden_word))
    else:
        attempts -= 1
        print(f"Wrong letter! You have {attempts} attempts.")

    if '_' not in hidden_word:
        print("You Won!! The word was:", random_word)
        break
if attempts == 0:
    print(f"You Lost! The word was: {random_word}")
