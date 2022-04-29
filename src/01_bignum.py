# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
x = 2
y = 65536
z = 1
print(x**y)
print()

# Less practical other way to do it
for i in range(0,y):
    z = z*x

print(z)