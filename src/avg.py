numbers = [1, 41, 34, 29, 50]

# assume ints has at least 3 integers
def  centered_avg(ints):
    #determine smallest element 
    small = min(ints)
    #determine largest element 
    large = max(ints)

    #sum all elements
    sum = 0 
    for i in ints:
        sum += i
    #sub largest and smallest from sum
    sum = sum - small- large
    #avg - divide by len  -2
    return sum / (len(ints)-2)
    #num elements -2

print(centered_avg(numbers))