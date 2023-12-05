numbers = "0123456789"

all_numbers = []
with open("Day1\Day1input.txt") as file:
    for line in file:
        first = "-100"
        last = "-100"
        count = -1
        for item in line:
            if item in numbers:
                count += 1
                if count == 0:
                    first = item
                    last = item
                else:
                    last = item
        number = first + last
        all_numbers.append(number)

all_added = 0
for num in all_numbers:
    all_added += int(num)
print(all_added)