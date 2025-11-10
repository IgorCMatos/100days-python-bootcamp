import random
from data import Country


def compare_country(Country1, Country2):
    if Country[Country1] > Country[Country2]:
        country_with_more_people = Country1
    else:
        country_with_more_people = Country2

    return country_with_more_people


game = True
score = 0
Country1 = random.choice(list(Country.keys()))

while game:
    Country2 = random.choice(list(Country.keys()))
    while Country1 == Country2:
        Country2 = random.choice(list(Country.keys()))
    print(f"Which one has the bigger population? {Country1} or {Country2}")
    user_choice = input("Type the name of the Country: ").title().strip()

    country_with_more_people = compare_country(Country1, Country2)

    if user_choice == country_with_more_people:
        score += 1
        print(f"Correct! Your score now is {score}")
        Country1 = Country2
    else:
        print(
            f"Wrong! The correct answer is {country_with_more_people}, your score is  {score}.")
        game = False
