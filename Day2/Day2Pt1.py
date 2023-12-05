MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


count = 0

def check_marbles(number_color, good_marbles):
    # number_color = int(number_color)
    if number_color[1].strip() == "red":
        if int(number_color[0]) > MAX_RED:
            good_marbles = False

    elif number_color[1].strip() == "green":
        if int(number_color[0]) > MAX_GREEN:
            good_marbles = False

    elif number_color[1].strip() == "blue":
        if int(number_color[0]) > MAX_BLUE:
            good_marbles = False

    return good_marbles


with open("Day2\Day2input.txt") as file:
    for line in file:
        good_marbles = True

        line_parts = line.split(": ")
        
        id = int(line_parts[0][4:])
        
        
        games = line_parts[1].split("; ")
        for game in games:
            cube_counts = game.split(", ")
            
            for cube_count in cube_counts:
                number_color = cube_count.split(" ")

                good_marbles = check_marbles(number_color, good_marbles)
        
        if good_marbles:
            count += id

print(count)


        


