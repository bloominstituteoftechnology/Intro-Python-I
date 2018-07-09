# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"

for i in num:
    if int(i) % 2 == 0:
        print("Even!")
    if int(i) % 2 != 0:
        print("Odd!")
    