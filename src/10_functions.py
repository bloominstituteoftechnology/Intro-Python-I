# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
    return x % 2 == 0

print(is_even(4))
print(is_even(3))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num) is True:
    print('Even!')
else:
    print('Odd')
