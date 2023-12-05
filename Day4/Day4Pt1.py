final_count = 0
with open("Day4/Day4input.txt") as file:
    for line in file:
        count = 0
        

        winning_yours = line[10:].split(" | ")

        winning_numbers = winning_yours[0].split(" ")
        your_numbers = winning_yours[1].split(" ")

        for num in your_numbers:
            num = num.strip()
            if num.isdigit():
                if num in winning_numbers:
                    count += 1


        if count != 0:
            final_count += (2 ** (count-1)) 
print(final_count)
