import multiprocessing

instructions = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"

foo_string = ""
for foo in instructions:
    if foo == "L":
        foo_string += "0"
    else:
        foo_string += "1"

instructions = foo_string




def main():
    
    start = []
    
    empty = {}
    path_dict = make_path_dict(empty)
    for path in path_dict.keys():
        # print(path)
        if path[2] == "A":
            start.append(path)

    # print(start)
    

    keep_going = True
    count = 0

    x0, y0, z0 = start[0]
    x1, y1, z1 = start[1]
    x2, y2, z2 = start[2]
    x3, y3, z3 = start[3]
    x4, y4, z4 = start[4]
    x5, y5, z5 = start[5]


    while keep_going:

        for instruction in instructions:
            count += 1
            
            x0, y0, z0 = path_dict[f"{x0}{y0}{z0}"][int(instruction)]
            x1, y1, z1 = path_dict[f"{x1}{y1}{z1}"][int(instruction)]
            x2, y2, z2 = path_dict[f"{x2}{y2}{z2}"][int(instruction)]
            x3, y3, z3 = path_dict[f"{x3}{y3}{z3}"][int(instruction)]
            x4, y4, z4 = path_dict[f"{x4}{y4}{z4}"][int(instruction)]
            x5, y5, z5 = path_dict[f"{x5}{y5}{z5}"][int(instruction)]
            

            if new_all_same([(x0, y0, z0), (x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4), (x5, y5, z5)]):
                keep_going = False
                break
            # print(start[0][2])

            # keep_going = False
            # break

    print(count)


def all_same(start):
    # print(start[0][2])
    return set(item[2] for item in start) == {"Z"}
        
    
def new_all_same(start):
    # print(start[0][2])
    count = 0
    for item in start:
        if item[2] == "Z":
            count += 1
        
    if count > 2:
        return True    
    else:
        return False

def make_path_dict(path_dict):
    with open("Day8/Day8input.txt") as file:
        for line in file:
            line.strip()
            parts = line.split(" = ")
            key = parts[0]

            L_R = parts[1].split(", ")
            left = L_R[0][1:]
            right = L_R[1][:3]
            value = [left, right]

            path_dict[key] = value
    return path_dict

if __name__ == "__main__":
    main()