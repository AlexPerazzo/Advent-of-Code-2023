def extra_backwards(extra):
    #extra = [largest, large, medium, small, smallest]
    #extra.reverse() = [smallest, small, medium, large, largest]
    extra = extra[::-1]
    subtractor = extra[0]
    for i in range(1, len(extra)):
        subtractor = extra[i] - subtractor

    return subtractor

def main():
    all_values = []
    with open("Day9/Day9input.txt") as file:
        for line in file:
            line = line.strip()
            numbers = line.split(" ")

            extra = []
            extra.append(int(numbers[0]))
            while not all(element == 0 for element in numbers):
                differences1 = []
                for i in range(len(numbers)-1):
                    differences1.append(int(numbers[i+1]) - int(numbers[i]))
                numbers = differences1
                extra.append(numbers[0])
                print(differences1)
            print(extra)
            add_this = extra_backwards(extra)
            all_values.append(add_this)

    print((sum(all_values)))





main()