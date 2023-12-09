import multiprocessing
def all_same(start):
    # print(start[0][2])
    return set(item[2] for item in start) == {"Z"}
        
    
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
for path in path_dict.keys():
    # print(path)
    if path[2] == "A":
        start.append(path)


def process_instruction(args):
    start, path_dict, instruction = args

    # Extract coordinates from the current state
    x0, y0, z0 = start[0]
    x1, y1, z1 = start[1]
    x2, y2, z2 = start[2]
    x3, y3, z3 = start[3]
    x4, y4, z4 = start[4]
    x5, y5, z5 = start[5]

    # Update coordinates using path_dict
    x0, y0, z0 = path_dict[f"{x0}{y0}{z0}"][int(instruction)]
    x1, y1, z1 = path_dict[f"{x1}{y1}{z1}"][int(instruction)]
    x2, y2, z2 = path_dict[f"{x2}{y2}{z2}"][int(instruction)]
    x3, y3, z3 = path_dict[f"{x3}{y3}{z3}"][int(instruction)]
    x4, y4, z4 = path_dict[f"{x4}{y4}{z4}"][int(instruction)]
    x5, y5, z5 = path_dict[f"{x5}{y5}{z5}"][int(instruction)]

    return [(x0, y0, z0), (x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4), (x5, y5, z5), z0]

def main():
    # Your existing code to set up start, instructions, and path_dict
    keep_going = True
    count = 0
    # Create a Pool with the number of available CPU cores
    while keep_going:
        with multiprocessing.Pool() as pool:
            # Use the pool to map the function to each instruction in parallel
            results = pool.map(process_instruction, [(start, path_dict, instruction) for instruction in instructions])
            count +=269
        # Extract the final state after all instructions
        final_state = results[-1]

        # Extract the z values from the final state
        z_values = final_state[:-1]

        # Check if all z values are equal
        if all(z == 'Z' for z in z_values):
            print("All z values are equal")
            keep_going = False
        else:
            print("Not all z values are equal")
            print(count)

if __name__ == "__main__":
    main()
