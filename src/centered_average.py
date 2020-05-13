# Return the :centered average of an array of ints,
# which we'll say is the mean of the values,
# except ignoring the largest and smallese values in the array

# centered_average([1, 2, 3, 4, 100]) 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) 5
# centered)average([-10, -4, -2, -4, -2, 0]) -3

# UNDERSTAND
# mean: sum divided by quantity: 2, 3, 4 --> 3
# are arrays sorted? NO
# are all values different, or are some duplicates? Some are duplicates
# assumption: we will always have 3 or more values
# No mutating the list
# There may be non integers
# We can use modules that aren't included

# PLAN
# find the min and max
# sum the list then subtract the min and max
# divide by the length of the list-2

# EXECUTE
def centered_average(numlist):
    lowest = min(*numlist)
    highest = max(*numlist)
    total = sum(numlist) - lowest - highest
    quantity = len(numlist) - 2
    return total / quantity

print(centered_average([1, 2, 3, 4, 100]))