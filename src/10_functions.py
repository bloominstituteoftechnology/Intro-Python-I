# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False


        
# Read a number from the keyboard

num = input("Enter a number: ")
num = int(num)

print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_still_even(num):
    if (num % 2) == 0:
        return "Even!"
    else:
        return "Odd"

num = input("Enter a number: ")
num = int(num)

print(is_still_even(num))