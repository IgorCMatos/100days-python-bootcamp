def calculate_love_score(name1, name2):
    sum_name = name1 + name2
    word1 = "love"
    word2 = "true"
    love_count = 0
    true_count = 0

    for char in word1:
        love_count += sum_name.count(char)
        
    for char in word2:
        true_count += sum_name.count(char)

    love_score = str(true_count) + str(love_count)
    print(love_score)


name1 = input("Type the first name:").lower().strip()
name2 = input("Type the second name:").lower().strip()

calculate_love_score(name1, name2)
