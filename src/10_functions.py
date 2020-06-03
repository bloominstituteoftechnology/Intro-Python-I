# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    number = abs(int(number))
    # number = abs(number)
    if number % 2 == 0:
        return True
    else:
        return False
            
# Read a number from the keyboard

print(is_even(-8))
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_or_odd(num):
    if is_even(num) == False:
        print("Odd")
    else:
        print("Even!")

even_or_odd(num)