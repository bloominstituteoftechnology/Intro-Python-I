# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")
number = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"

def isEven(number):
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd")
        
isEven(number)