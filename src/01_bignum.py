# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
n = 2

for i in range(1, 65537):
    n=2*n

print("The value of 2 to the 65536 power is: ", end="")
print(n)