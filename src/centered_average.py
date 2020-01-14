fromt typing import List
'''
Return the "centered" average of an array of ints,
which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array
'''

# centered_average([1, 2, 3, 4, 100]) -> 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) -> 5
# centered_average([-10, -4, -2, -4, -2, 0]) -> -3

def centered_avg(ints: List[int]) -> int:
    # copies list of ints by value
    ints_copy = ints.copy()

    # sort the ints
    # this is a computationally expensive action
    ints_copy.sort()

    # slice off the first and last value
    ints_copy = ints_copy[1:-1]

    # sum the remaining values and divide by the length of the list
    return sum(ints_copy) // len(ints_copy)

def centered_avg_semi_optimized(ints: List[int]) -> int:
    ints_copy = ints.copy()
    # find the max and min value
    smallest = min(ints_copy)
    largest = max(ints_copy)

    # remove max and min
    ints_copy.remove(smallest)
    ints_copy.remove(largest)

    # find sum of new array // length of new array
    return sum(ints_copy) // len(ints_copy)

def centered_avg_optimized(ints: List[int]) -> int:
    largest = ints[0]
    smallest = ints[0]
    total = 0

    # for integer in ints
    for n in ints:
        # if the integer is smaller than min,
        # set min to the int
        if n < smallest:
            smallest = n
        # if the integer is larger than max,
        # set max to the int
        if n > largest:
            largest = n
        
        # keep a running total of the sum
        total += n

    # return the sum minus the largest and smallest divided by the length - 2
    return (total - largest - smallest) // (len(ints) - 2)
