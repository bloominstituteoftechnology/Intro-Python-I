"""
Program that asks for a number from the user, and returns whether 
that number is even or odd.
"""

# Write a function is_even that will return true if the passed-in number is even.
def is_even(number:int):
    """
    Determines if the input integer is an even number or not.
    """
    if number % 2 == 0:
        return True
    else:
        return False

# Get a number from the keyboard as user input:
while True:
    num = input("Enter a number: ")
    try:
        num = int(num)
        break
    except ValueError as value_error:
        print(f"Cannot accept this input. Please enter an integer.\n")

# Print out "Even!" if the number is even. Otherwise print "Odd":
if is_even(number=num):
    print("Even\n")
else:
    print("Odd\n")
