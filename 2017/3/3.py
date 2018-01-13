j"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8 3^2  10
21  22  23  24 5^2
..  ..  ..  ..  .. 7^2        
"""

import math 
import itertools

input = 361527

def side_length(number):
    side = math.ceil(math.sqrt(number))
    side = side if side % 2 != 0 else side + 1
    return side

side = side_length(input)
steps_to_reach_center_from_axis = (side-1)/2
axises = [side**2 - ((side-1) * i)  - math.floor(side/2) for i in range(0, 4)] #get the axis "cells"
steps_to_reach_axix_from_input = min([abs(axis - input) for axis in axises])

print(steps_to_reach_axix_from_input + steps_to_reach_center_from_axis)



nine_directions = list(itertools.product(range(-1, 1 + 1), range(-1, 1 + 1)))

def solve2(input_num):
    def sum_adjacents(x, y):
        numbers[x][y] = sum(
            [numbers[x + n[0]][y + n[1]] for n in nine_directions])

    sq = int(input_num ** 0.5) + 1  # big enough
    numbers = [[0 for i in range(sq * 2)] for j in range(sq * 2)]

    current_number = 1
    x = y = sq
    numbers[x][y] = current_number
    delta = 0

    four_directions = [(+1, 0), (0, +1), (-1, 0), (0, -1)]  # right up left down
    while numbers[x][y] <= input_num:
        n_i = 0
        for _ in range(2):
            for _ in range(2):
                for i in range(delta):
                    current_number += 1
                    direction = four_directions[n_i]
                    x += direction[0]
                    y += direction[1]
                    sum_adjacents(x, y)
                    if numbers[x][y] > input_num:
                        print("answer 2: ", numbers[x][y])
                        return
                n_i += 1
            delta += 1


solve2(361527)
# part 2 inbitable
# def sum_spiral():
#     a, i, j = {(0,0) : 1}, 0, 0
#     sn = lambda i,j: sum(a.get((k,l), 0) for k in range(i-1,i+2)
#                                          for l in range(j-1,j+2))
#     for s in count(1, 2):
#         for _ in range(s):   i += 1; a[i,j] = sn(i,j); yield a[i,j]
#         for _ in range(s):   j -= 1; a[i,j] = sn(i,j); yield a[i,j]
#         for _ in range(s+1): i -= 1; a[i,j] = sn(i,j); yield a[i,j]
#         for _ in range(s+1): j += 1; a[i,j] = sn(i,j); yield a[i,j]

# def part2(n):
#     for x in sum_spiral():
#         if x>n: return x