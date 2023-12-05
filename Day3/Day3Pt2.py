def main():
    all_nums = []
    line_list = []
    gear_numbers = []
    with open("Day3/Day3input.txt") as file:
        for line in file:
            line_list.append(line)





    y_axis = -1
    # x_axis = -1
    with open("Day3/Day3input.txt") as file:
        for line in file:
            line = line.strip()
            x_axis = -1
            y_axis += 1
            for thing in line:
                x_axis += 1
                thing = thing.strip()

                if (not thing.isdigit()) and (thing != "."):
                    # print(thing)
                    
                    nums = []
                    for i in range(8):
                        num = []
                        num_x_y = check_surrondings_for_num(x_axis, y_axis, line_list, i)
                        if num_x_y[0].isdigit():
                            
                            num.append(num_x_y[0])
                            num = check_left_of_num(num_x_y[1], num_x_y[2], line_list, num)
                            num = check_right_of_num(num_x_y[1], num_x_y[2], line_list, num)
                            # print(num)
                            if num:
                                if "".join(num) not in nums:
                                    nums.append("".join(num))
                    
                    if len(nums) == 2 and thing == "*":
                        gear_numbers.append(int(nums[0]) * int(nums[1]))

                    print(nums)
                    for number in nums:
                        all_nums.append(number)
                        

    total_count = 0
    for item in all_nums:
        item = int(item)
        total_count += item

    print(total_count)

    gear_total = 0
    for gear in gear_numbers:
        gear_total += gear
    print(gear_total)




#recursively go down left side of number
def check_left_of_num(x_axis, y_axis, line_list, num):
    
    if x_axis - 1 < 0:
        return num
    
    num_to_check = line_list[y_axis][x_axis - 1]

    if not num_to_check.isdigit():
        return num

    else:
        num.insert(0, num_to_check)
        return check_left_of_num(x_axis - 1, y_axis, line_list, num)

#recursively go down right side of number
def check_right_of_num(x_axis, y_axis, line_list, num):

    if x_axis + 1 > len(line_list[y_axis]):
        return num
    
    num_to_check = line_list[y_axis][x_axis + 1]

    if not num_to_check.isdigit():
        return num 

    else:
        num.append(num_to_check)
        return check_right_of_num(x_axis + 1, y_axis, line_list, num)


def check_surrondings_for_num(x_axis, y_axis, line_list, placement):
    #returns surronding objects depending on placement around center num
    if placement == 0:
        return (line_list[y_axis - 1][x_axis - 1], x_axis - 1, y_axis - 1)
    elif placement == 1:
        return (line_list[y_axis - 1][x_axis], x_axis, y_axis - 1)
    elif placement == 2:
        return (line_list[y_axis - 1][x_axis + 1], x_axis + 1, y_axis - 1)
    elif placement == 3:
        return (line_list[y_axis][x_axis - 1], x_axis - 1, y_axis)
    elif placement == 4:
        return (line_list[y_axis][x_axis + 1], x_axis + 1, y_axis,)
    elif placement == 5:
        return (line_list[y_axis + 1][x_axis - 1], x_axis - 1, y_axis + 1)
    elif placement == 6:
        return (line_list[y_axis + 1][x_axis], x_axis, y_axis + 1)
    elif placement == 7:
        return (line_list[y_axis + 1][x_axis + 1], x_axis + 1, y_axis + 1,)


main()