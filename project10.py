"""
Projeto sobre 
"""

import random


def card_deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card


def sum_card(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(p_result, c_result):
    if p_result == c_result:
        return "Draw"
    elif c_result == 0:
        return "You Lose, opponent has Blackjack"
    elif p_result == 0:
        return "You Win, you have a Blackjack"
    elif c_result > 21:
        return "Opponent went over. You Win"
    elif p_result > 21:
        return "You went over. You Lose"
    elif p_result > c_result:
        return "You win"
    else:
        return "You Lose"


def game():
    player_card = []
    computer_card = []
    computer_result = -1
    player_result = -1
    game_over = False

    for _ in range(2):
        player_card.append(card_deal())
        computer_card.append(card_deal())

    while not game_over:
        player_result = sum_card(player_card)
        computer_result = sum_card(computer_card)
        print(f"Your cards: {player_card}, Total: {player_result}")
        print(f"Computer's card: {computer_card[0]}")

        if player_result == 0 or computer_result == 0 or player_result > 21:
            game_over = True
        else:
            more_card = input(
                "Type 'yes' or 'no', if you want to get another card: ")
            if more_card == 'yes':
                player_card.append(card_deal())
            else:
                game_over = True

    if player_result <= 21:
        while computer_result != 0 and computer_result < 17:
            computer_card.append(card_deal())
            computer_result = sum_card(computer_card)

    print(f"Your final hand: {player_card}, score: {player_result}")
    print(f"Computer's final hand: {computer_card}, score: {computer_result}")
    print(compare(player_result, computer_result))


while input("Do you want to play a game of Blackjack? 'yes' or 'no '") == "yes":
    print("\n" * 100)
    game()
