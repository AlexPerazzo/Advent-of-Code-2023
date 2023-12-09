import multiprocessing



def main(thing):
    

    pool = multiprocessing.Pool(6)
    keep_going = True
    count = 0
    while keep_going:
        for instruction in instructions:
            count += 1
            
            
            holder = pool.starmap(swap_start, [(task, instruction) for task in thing])
            # pool.map(swap_start, args=(start, instruction))

            start = holder
            pool.close()
            pool.join()
            

            if all_same(start):
                keep_going = False
                break
            # print(start[0][2])

            # keep_going = False
            # break

    print(count)

def swap_start(task, instruction):
    task = path_dict[task][int(instruction)]

def all_same(start):
    print(start[4][2])
    if (start[0][2] == "Z") and (start[1][2] == "Z") and (start[2][2] == "Z") and (start[3][2] == "Z") and (start[4][2] == "Z") and (start[5][2] == "Z"):
        return True
    else:
        return False
    
def new_all_same(start):
    # print(start[0][2])
    count = 0
    for item in start:
        if item[2] == "Z":
            count += 1
        
    if count > 3:
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


instructions = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"

foo_string = ""
for foo in instructions:
    if foo == "L":
        foo_string += "0"
    else:
        foo_string += "1"

instructions = foo_string

start = []
empty = {}
path_dict = make_path_dict(empty)
# print(path_dict)
for path in path_dict.keys():
        # print(path)
    if path[2] == "A":
        start.append(path)
print(start)

thing = start

if __name__ == "__main__":
    main(thing)