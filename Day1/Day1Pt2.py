# def build_table(pattern, inputs):
#     table = []

#     for k in range(len(pattern) + 1):
#         char_map = {}

#         for letter in inputs:
#             pk_letter = pattern[:k] + letter
#             temp = [k + 1, len(pattern)]
#             i = min(temp)

#             while not pk_letter.endswith(pattern[:i]):
#                 i -= 1

#             char_map[letter] = i

#         table.append(char_map)

#     return table


# def string_matcher(text, pattern, inputs):
#     table = build_table(pattern, inputs)
#     state = 0
#     match_state = len(table) - 1
#     results = []

#     for index in range(len(text)):
#         state = table[state][text[index]]

#         if state == match_state:
#             results.append(index)
#             state = 0  # Reset the state to 0 after a match

#     return results

def check_for_written_numbers(line, written_numbers):
    # for letter in line:
    return


def main():
    numbers = "0123456789"
    written_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    all_numbers = []
    with open("Day1\Day1input.txt") as file:

        for line in file:
            first = "-100000000"
            last = "-100000000"
            count = -1
            
            line = line.replace("one", "one1one")
            line = line.replace("two", "two2two")
            line = line.replace("three", "three3three")
            line = line.replace("four", "four4four")
            line = line.replace("five", "five5five")
            line = line.replace("six", "six6six")
            line = line.replace("seven", "seven7seven")
            line = line.replace("eight", "eight8eight")
            line = line.replace("nine", "nine9nine")

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

main()