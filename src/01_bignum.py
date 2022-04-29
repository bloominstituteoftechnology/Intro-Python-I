# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE

# a = 2 ** 65536

a = pow(2, 65536)
print(a)


def is_even(num):
    if num % 2 == 0:
        return True
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num) == True:
    print("Even")
else:
    print("Odd")