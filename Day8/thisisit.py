import math
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
    starts = []
    
    empty = {}
    path_dict = make_path_dict(empty)
    for path in path_dict.keys():
        # print(path)
        if path[2] == "A":
            starts.append(path)
    
    empty = {}
    path_dict = make_path_dict(empty)
    all_counts = []

    for start in starts:
        count = 0
        # print(start)
        while start[2] != "Z":
            for instruction in instructions:
                count += 1
                start = path_dict[start][int(instruction)]
                # print(start)
                if start[2] == "Z":
                    break
        all_counts.append(count)
        print(count)

    # Example: LCM of 2, 3, 4, 6, 8, and 12
    
    result = lcm_of_numbers(all_counts)
    print(f"The LCM of {all_counts} is {result}")
    



def make_path_dict(path_dict):
    with open("Day8/Day8input.txt") as file:
        for line in file:
            parts = line.split(" = ")
            key = parts[0]

            L_R = parts[1].split(", ")
            left = L_R[0][1:]
            right = L_R[1][:3]
            value = [left, right]

            path_dict[key] = value
    return path_dict


import math

def prime_factors(n):
    factors = []
    # Divide by 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Divide by odd numbers starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors

def lcm_of_numbers(numbers):
    all_factors = {}
    
    # Find prime factors for each number
    for num in numbers:
        factors = prime_factors(num)
        for factor in set(factors):
            if factor not in all_factors or factors.count(factor) > all_factors[factor]:
                all_factors[factor] = factors.count(factor)

    # Calculate LCM
    lcm = 1
    for factor, exponent in all_factors.items():
        lcm *= factor ** exponent

    return lcm




main()