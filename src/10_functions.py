# Write a function is_even that will return true if the passed-in number is even.

def is_even(n):
    if n % 2 == 0:
        print("Even!")
    else:
        print("Odd")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

print(is_even(num))

