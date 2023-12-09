instructions = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"

foo_string = ""
for foo in instructions:
    if foo == "L":
        foo_string += "0"
    else:
        foo_string += "1"

instructions = foo_string




def main():
    END = "ZZZ"
    start = "AAA"
    empty = {}
    path_dict = make_path_dict(empty)


    count = 0
    while start != END:
        for instruction in instructions:
            count += 1
            start = path_dict[start][int(instruction)]
            if start == END:
                break
        print(count)

    print(count)

        

def make_path_dict(path_dict):
    with open("Day8/Day8input.txt") as file:
        for line in file:
            parts = line.split(" = ")
            key = parts[0]

            L_R = parts[1].split(", ")
            left = L_R[0][1:]
            right = L_R[1][:-2]
            value = [left, right]

            path_dict[key] = value
    return path_dict

main()