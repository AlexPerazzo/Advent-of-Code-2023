final_count = 0
all_my_cards_dict = {}
memoization_dict = {}
line_count = 0
line_count2 = 0

with open("Day4/Day4input.txt") as file:
    # initalize the two dictionaries. One of each card. Currently each points is at 0 (because they haven't been checked yet)
    for line in file:
        line_count += 1
        all_my_cards_dict[line_count] = 1
        memoization_dict[line_count] = 0


with open("Day4/Day4input.txt") as file:
    for line in file:
        count = 0
        line_count2 += 1
        

        winning_yours = line[10:].split(" | ")

        winning_numbers = winning_yours[0].split(" ")
        your_numbers = winning_yours[1].split(" ")

        for num in your_numbers:
            num = num.strip()
            if num.isdigit():
                if num in winning_numbers:
                    count += 1

        memoization_dict[line_count2] = count
        # print(memoization_dict[line_count2])

# print(line_count)
# print(line_count2)

for i in range(1, line_count + 1):
    # remember how many additional cards to add
    points = memoization_dict[i]

    # remember how many times you have to add those addtional cards
    how_many = all_my_cards_dict[i]
    for j in range(1, points + 1):
        all_my_cards_dict[i + j] += 1 * how_many

total_scratch_cards = 0
for i in range(1, line_count + 1):
    total_scratch_cards += all_my_cards_dict[i]

print(total_scratch_cards)


        
