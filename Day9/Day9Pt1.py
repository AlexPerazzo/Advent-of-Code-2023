

all_values = []
with open("Day9/Day9input.txt") as file:
    for line in file:
        line = line.strip()
        numbers = line.split(" ")

        extra = []
        extra.append(int(numbers[-1]))
        while not all(element == 0 for element in numbers):
            differences1 = []
            for i in range(len(numbers)-1):
                differences1.append(int(numbers[i+1]) - int(numbers[i]))
            numbers = differences1
            extra.append(numbers[-1])
            print(differences1)
            # print(extra)
        all_values.append(sum(extra))

print((sum(all_values)))

