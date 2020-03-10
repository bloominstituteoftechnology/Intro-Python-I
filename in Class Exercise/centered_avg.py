# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(arr):
    # I would set the array and sort it
    arr.sort()
    # then remove smallest and largest
    arr.pop()
    arr.pop(0)
    # Return the sum divided by the length of the remaining elements
    return sum(arr) // len(arr)

centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7])
centered_average([-10, -4, -2, -4, -2, 0])


def centered_average(arr):
    # remove min and max
    arr.remove(min(arr))
    arr.remove(max(arr))
    # Return the sum divided by the length of the remaining elements
    return sum(arr) // len(arr)



def centered_average(arr):
    total = 0
    min_value = arr[0]
    max_value = arr[0]
    # I would go through the list iterating from both ends,
    for num in arr:
        # finding the largest and smallest,
        # adjusting for when we find a new min/max.
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
        # and maintaining the sum of the remaining elements,
        total += num
    # subtract the elements instead of removing them from the array
    return (total - max_value - min_value) // (len(arr) - 2)

