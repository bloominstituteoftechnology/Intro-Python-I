# Write a function is_even that will return true if the passed-in number is even.


def is_even(n):
    return n % 2 == 0


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def print_reults(num):
    if is_even(num):
        print(f"{num} is Even!")
    else:
        print(f"{num} is Odd!")


print_reults(num)
