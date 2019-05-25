# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
n = 2
exponent = 0

while exponent < 16+1:
    res = n ** exponent
    exponent = exponent + 1
    print(res)
