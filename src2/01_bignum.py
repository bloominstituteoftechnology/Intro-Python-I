# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
# print(2 ** 65536)

numbers = [num ** 2 for num in range(101)]
print(numbers)
print()
divisibles_of2 = [num // 2 for num in reversed(range(25))]
print(divisibles_of2)

factors_of3 = [num * 3 for num in range(13)]
print(factors_of3)

