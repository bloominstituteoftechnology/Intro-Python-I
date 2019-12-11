# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

print(is_even(10))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

def is_even2(x):
    if x%2 == 0:
        print("Even!")

    else:
        print("Odd")

is_even2(num)
