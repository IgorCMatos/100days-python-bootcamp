def life_in_weeks(age):
    remain_age = 90 - age
    remain_weeks = remain_age * 52
    print(f"You have {remain_weeks} weeks left.")


age = int(input("How old are you?"))

life_in_weeks(age)
