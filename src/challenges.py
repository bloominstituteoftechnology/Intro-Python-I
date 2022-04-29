"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring
the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy,
and likewise for the largest value. Use int division to produce the final average. You may assume that the array is
length 3 or more.
"""
def centered_average(list):
    centered_total = sum(list) - min(list) - max(list)
    centered_len = len(list) - 2

    return  (centered_total // centered_len)


numbers = [-100, 2, 3, 4, 5, 6, 5000]
print(centered_average(numbers))

print(centered_average([1, 2, 3, 4, 100])) # → 3
print(centered_average([1, 1, 5, 5, 10, 8, 7])) # → 5
print(centered_average([-10, -4, -2, -4, -2, 0])) # → -3

"""
sort them (keeping duplicates),
total all but first and last
return total // len() - 2
"""