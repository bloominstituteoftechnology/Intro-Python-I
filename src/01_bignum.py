# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE

# create a variable to store the result
n = 1 
base = 2

# use for loop to count until 65536
for i in range(0, 65536):
    # multiply the base
    n = n * base
print(n)

