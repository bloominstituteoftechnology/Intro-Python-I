# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even2(number):
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd")

outcome = is_even(num)
print(outcome)
is_even2(num)