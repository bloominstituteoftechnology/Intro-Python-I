'''
Given a 6x6 2D array, arr

abcdef
ijklmn
opqurs
tuvwxy
z01234
6789!@

An hourglass is
abc
 d
efg

16 hourglasses in arr
Calculate each hourglass sum
Return the max value of those.

'''
# Make a hourglass_sums array
# Then find the hourglasses
#   Move through arr x[0] - x[3], y[0] - y[3] to get upper left of each hourglass
#   Find the sum of the hourglass values.
# Add that sum to hourglass_sums array
# Return the max value

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    # hourglass_count = 0 # If you want to make sure you are getting all of the hourglasses
    hourglass_sums = []

    hourglass_sum = arr[0][0]
    '''
    # Just to print out the first hourglass to see that I'm using the indices correctly
    print(
        f'{arr[0][0]} {arr[0][1]} {arr[0][2]} \n  {arr[1][1]}\n{arr[2][0]} {arr[2][1]} {arr[2][2]}')
    '''
    for i in range(0, 4):
        for j in range(0, 4):  # i <- y, j <-x
            # Top row
            hourglass_sum = arr[i][j]
            hourglass_sum += arr[i][j+1]
            hourglass_sum += arr[i][j+2]

            # Middle
            hourglass_sum += arr[i+1][j+1]

            # Bottom
            hourglass_sum += arr[i+2][j]
            hourglass_sum += arr[i+2][j+1]
            hourglass_sum += arr[i+2][j+2]
            hourglass_sums.append(hourglass_sum)
            # print("hourglass_sum_final :" + str(hourglass_sum))
            # hourglass_count += 1

    # print("hourglass_count: " + str(hourglass_count))
    # print(hourglass_sums)
    return(max(hourglass_sums))


print(hourglassSum([[-9, -9, -9,  1, 1, 1],
                    [0, -9,  0,  4, 3, 2],
                    [-9, -9, -9,  1, 2, 3],
                    [0,  0,  8,  6, 6, 0],
                    [0,  0,  0, -2, 0, 0],
                    [0,  0,  1,  2, 4, 0]]))

'''
hourglassSum([[0, 1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10, 11],
              [12, 13, 14, 15, 16, 17],
              [18, 19, 20, 21, 22, 23],
              [24, 25, 26, 27, 28, 29],
              [30, 31, 32, 33, 34, 35]])
'''
