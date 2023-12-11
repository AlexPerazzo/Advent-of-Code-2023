

def main():
    pipe_maze = make_pipe_maze()
    x_cord, y_cord = where_is_S(pipe_maze)
    symbol, x_cord, y_cord = check_around_S(pipe_maze, x_cord, y_cord)
    print(x_cord)
    print(y_cord)
    count = 0

    while symbol != "S":
       
        pipe_maze, x_cord, y_cord, symbol, count = follow_pipe(pipe_maze, x_cord, y_cord, symbol, count)

    print((count+1)/2)



def follow_pipe(pipe_maze, x_cord, y_cord, symbol, count):
    if y_cord-1 >= 0:
        north = pipe_maze[y_cord-1][x_cord]
    else:
        north = "0"
    if x_cord+1 <= 139:
        east = pipe_maze[y_cord][x_cord+1]
    else:
        east = "0"
    if y_cord+1 <= 139:
        south = pipe_maze[y_cord+1][x_cord]
    else:
        south = "0"
    if x_cord-1 >= 0:
        west = pipe_maze[y_cord][x_cord-1]
    else:
        west = "0"
    count += 1
    pipe_maze[y_cord][x_cord] = "0"
    
    if symbol == "7":
        if south != "0" and south != "S":
            
            symbol = south
            return pipe_maze, x_cord, y_cord+1, symbol, count
        
        elif west != "0" and west != "S":
            
            symbol = west
            return pipe_maze, x_cord-1, y_cord, symbol, count
        
        else:
            symbol = "S"
            return pipe_maze, x_cord, y_cord, symbol, count

    elif symbol == "F":
        if south != "0" and south != "S":
            
            
            symbol = south
            return pipe_maze, x_cord, y_cord+1, symbol, count
        
        elif east != "0" and east != "S":
            
            symbol = east
            return pipe_maze, x_cord+1, y_cord, symbol, count
        
        else:
            symbol = "S"
            return pipe_maze, x_cord, y_cord, symbol, count

    elif symbol == "J":
        if north != "0" and north != "S":
            
            symbol = north
            return pipe_maze, x_cord, y_cord-1, symbol, count
        
        elif west != "0" and west != "S":
            
            symbol = west
            return pipe_maze, x_cord-1, y_cord, symbol, count
        
        else:
            symbol = "S"
            return pipe_maze, x_cord, y_cord, symbol, count


    elif symbol == "|":
        if north != "0" and north != "S":
            
            symbol = north
            return pipe_maze, x_cord, y_cord-1, symbol, count
        
        elif south != "0" and south != "S":
            
            symbol = south
            return pipe_maze, x_cord, y_cord+1, symbol, count
        
        else:
            symbol = "S"
            return pipe_maze, x_cord, y_cord, symbol, count
        
    
    elif symbol == "-":
        if east != "0" and east != "S":
            
            symbol = east
            return pipe_maze, x_cord+1, y_cord, symbol, count
        
        elif west != "0" and west != "S":
            
            symbol = west
            return pipe_maze, x_cord-1, y_cord, symbol, count
        
        else:
            symbol = "S"
            return pipe_maze, x_cord, y_cord, symbol, count
        
    elif symbol == "L":
        if east != "0" and east != "S":
            
            symbol = east
            return pipe_maze, x_cord+1, y_cord, symbol, count
        
        elif north != "0" and north != "S":
            
            symbol = north
            return pipe_maze, x_cord, y_cord-1, symbol, count
        
        else:
            symbol = "S"
            return pipe_maze, x_cord, y_cord, symbol, count

def check_around_S(pipe_maze, x_cord, y_cord):
    
    north = pipe_maze[y_cord-1][x_cord]
    east = pipe_maze[y_cord][x_cord+1]
    south = pipe_maze[y_cord+1][x_cord]
    west = pipe_maze[y_cord][x_cord-1]

    if north == "|" or north == "7" or north == "F":
        symbol = north
        return symbol, x_cord, y_cord-1
    
    elif east == "-" or east == "J" or east == "7":
        symbol = east
        return symbol, x_cord +1, y_cord

    elif south == "|" or south == "J" or south == "L":
        symbol = south
        return symbol, x_cord, y_cord+1

    elif west == "F" or west == "L" or west == "-":
        symbol = west
        return symbol, x_cord, y_cord-1


def where_is_S(pipe_maze):
    # x_cord = -1
    y_cord = -1

    for pipe_line in pipe_maze:
        y_cord += 1
        x_cord = -1
        for pipe in pipe_line:
            x_cord += 1
            if pipe == "S":
                return (x_cord, y_cord)

def make_pipe_maze():
    pipe_maze = []
    with open("Day10/Day10input.txt") as file:
        for line in file:
            line = line.strip()
            pipes = []
            for pipe in line:
                pipes.append(pipe)
            pipe_maze.append(pipes)
            # print(pipe_maze)
            
    


    return pipe_maze



main()
#function that intakes maze pipe's coordinates, and which direction the pipe is coming from.
#Use which direction the previous pipe is heading from to determine which direction to head to.
#Increase a counter until you hit the 'S'

# def follow_recursion(pipe_maze, x_cord, y_cord, direction_from, count):
#     north = pipe_maze[y_cord-1][x_cord]
#     east = pipe_maze[y_cord][x_cord+1]
#     south = pipe_maze[y_cord+1][x_cord]
#     west = pipe_maze[y_cord][x_cord-1]
#     count += 1

#  def recursion_helper(direction1, direction2):
#     if symbol == "-":
#         if direction1 != "0":
#             pipe_maze[y_cord][x_cord] = "0"
#             count += 1
#             symbol = east
#             return follow_recursion(pipe_maze, x_cord, y_cord, symbol, count)
        
#         elif direction2 != "0":
#             pipe_maze[y_cord][x_cord] = "0"
#             count += 1
#             symbol = south
#             return follow_recursion(pipe_maze, x_cord, y_cord, symbol, count)
        
#         else:
#             return count



#| is a vertical pipe connecting north and south.
#- is a horizontal pipe connecting east and west.
#L is a 90-degree bend connecting north and east.
#J is a 90-degree bend connecting north and west.
#7 is a 90-degree bend connecting south and west.
#F is a 90-degree bend connecting south and east.
#. is ground; there is no pipe in this tile.