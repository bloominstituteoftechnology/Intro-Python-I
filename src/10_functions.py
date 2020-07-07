# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):

    return (n % 2 == 0)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_odd(n):

    if n % 2 == 0:
        
        print("Even!")

    else:

        print("Odd")

if __name__ == "__main__":
    print(is_even(1))
    print(is_even(2))
    # Read a number from the keyboard
    num = input("Enter a number: ")
    num = int(num)
    even_odd(num)
    num = input("Enter a number: ")
    num = int(num)
    even_odd(num)

