
def main():
    universe, x_axis_insert_space_here, y_axis_insert_space_here = make_universe()
    print(x_axis_insert_space_here)
    print(y_axis_insert_space_here)
    all_galaxies = find_galaxies(universe)
    # print(all_galaxies)
    total_distance = 0

    for i in range(len(all_galaxies)):
        for j in range(i + 1, len(all_galaxies)):
            total_distance += calculate_distance(all_galaxies[i][0], all_galaxies[i][1], all_galaxies[j][0], all_galaxies[j][1], x_axis_insert_space_here, y_axis_insert_space_here)

    print(total_distance)

def find_galaxies(universe):
    all_galaxies = []
    y_cord = -1

    for line in universe:
        y_cord += 1
        x_cord = -1
        for item in line:
            x_cord += 1
            if item == "#":
                all_galaxies.append([x_cord, y_cord])
                
    return all_galaxies

def calculate_distance(x_cord1, y_cord1, x_cord2, y_cord2, x_axis_insert_space_here, y_axis_insert_space_here):
    additional_total = 0
    for num in x_axis_insert_space_here:
        if (num < x_cord1 and num > x_cord2) or (num > x_cord1 and num < x_cord2):
            additional_total += 999999

    for numb in y_axis_insert_space_here:
        if (numb < y_cord1 and numb > y_cord2) or (numb > y_cord1 and numb < y_cord2):
            additional_total += 999999

    # print(additional_total)
    return (abs(x_cord1 - x_cord2) + abs(y_cord1 - y_cord2) + additional_total)



def make_universe():
    def check_vertical_universe(universe):
        line_length = len(universe[0])
        x_axis_insert_space_here = []
        for i in range(line_length):
            no_galaxy = True
            for line in universe:
                if line[i] == "#":
                    no_galaxy = False
            if no_galaxy:
                x_axis_insert_space_here.append(i)

        return x_axis_insert_space_here
    
    universe = []
    y_axis_insert_space_here = []
    with open("Day11/Day11input.txt") as file:

        line_number = -1
        for line in file:
            line_number += 1
            line = line.strip()
            no_galaxy = True
            for item in line:
                if item == "#":
                    no_galaxy = False
            universe.append(line)
            if no_galaxy:
                y_axis_insert_space_here.append(line_number)

    
    x_axis_insert_space_here = check_vertical_universe(universe)
    return universe, x_axis_insert_space_here, y_axis_insert_space_here


main()