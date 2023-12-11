
def main():
    universe = make_universe()
    
    all_galaxies = find_galaxies(universe)

    total_distance = 0

    for i in range(len(all_galaxies)):
        for j in range(i + 1, len(all_galaxies)):
            total_distance += calculate_distance(all_galaxies[i][0], all_galaxies[i][1], all_galaxies[j][0], all_galaxies[j][1])

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

def calculate_distance(x_cord1, y_cord1, x_cord2, y_cord2):
    return (abs(x_cord1 - x_cord2) + abs(y_cord1 - y_cord2))


def make_universe():
    def check_vertical_universe(universe):
        line_length = len(universe[0])
        insert_space_here = []
        for i in range(line_length):
            no_galaxy = True
            for line in universe:
                if line[i] == "#":
                    no_galaxy = False
            if no_galaxy:
                insert_space_here.append(i)

        insert_space_here.reverse()

        # print(universe[0])
        new_universe = []
        for line in universe:
            for space in insert_space_here:
                line = list(line)
                line.insert(space, ".")
                line = "".join(line)
            new_universe.append(line)
        # print(new_universe[0])
        return new_universe
    
    universe = []

    with open("Day11/Day11input.txt") as file:
        for line in file:
            line = line.strip()
            no_galaxy = True
            for item in line:
                if item == "#":
                    no_galaxy = False
            universe.append(line)
            if no_galaxy:
                universe.append(line)

    

    return check_vertical_universe(universe)




main()