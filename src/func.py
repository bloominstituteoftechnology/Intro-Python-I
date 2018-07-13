# Write a function is_even that will return true if the passed number is even.

# Read a number from the keyboard
num = input("Please enter a number: ")
# print(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even(num):
    if int(num) % 2 == 0:
        print(num + " is even!")
    else:   
        print(num + " is odd!")

print(is_even(num))
