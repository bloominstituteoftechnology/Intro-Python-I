# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3


[ 1, 5, 5, 10, 8, 7]


x = sum([2, 3, 4]) //3
print(x)

y = sum([-4, -2, -4, -2]) //4
print(y)

def centered_average(arr):
    #set array and sort it
    #then remove the largest and the smallest
    #return the sum devided by num of items
    arr.sort()
    arr.pop()
    arr.pop(0)
    return sum(arr) // len(arr)

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))


def centered_average2(arr):
    arr.remove(min(arr))
    arr.remove(max(arr))

    return sum(arr) // len(arr)


print(centered_average2([1, 2, 3, 4, 100]))
print(centered_average2([1, 1, 5, 5, 10, 8, 7]))
print(centered_average2([-10, -4, -2, -4, -2, 0]))

def centered_average3(arr):
    total = 0
    min_value = float("inf")
    max_value = arr[0]

    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

        total += num
    # subtract the elements instead of removing them from the array
    return (total - max_value - min_value) // (len(arr) - 2)

print(centered_average3([1, 2, 3, 4, 100]))
print(centered_average3([1, 1, 5, 5, 10, 8, 7]))
print(centered_average3([-10, -4, -2, -4, -2, 0]))