
count = 0

def max_marbles(max_cubes, number_color):
    # number_color = int(number_color)
    if number_color[1].strip() == "red":
        if int(number_color[0]) > max_cubes[0]:
            max_cubes[0] = int(number_color[0])

    elif number_color[1].strip() == "green":
        if int(number_color[0]) > max_cubes[1]:
            max_cubes[1] = int(number_color[0])

    elif number_color[1].strip() == "blue":
        if int(number_color[0]) > max_cubes[2]:
            max_cubes[2] = int(number_color[0])

    return max_cubes

def calculate_power(max_cubes):
    return max_cubes[0] * max_cubes[1] * max_cubes[2]


with open("Day2\Day2input.txt") as file:
    for line in file:
        good_marbles = True
        max_cubes = [0,0,0]

        line_parts = line.split(": ")
        
        
        
        games = line_parts[1].split("; ")
        for game in games:
            cube_counts = game.split(", ")
            
            for cube_count in cube_counts:
                number_color = cube_count.split(" ")

                max_cubes = max_marbles(max_cubes, number_color)

        power = calculate_power(max_cubes)
        
        count += power

print(count)


        


