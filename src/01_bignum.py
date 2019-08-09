# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
print(pow(2,65536))

product = 1
for i in range(0,65536):
    product = 2*product

print(product)
