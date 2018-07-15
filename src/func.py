# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"


def even_odd(num):
    ans1 = "Even!"
    ans2 = "Odd!"
    default = f"{num} is not a number!"
    if (num).isdigit() == False:
        return default
    elif int(num) % 2 == 0:
        return ans1
    else:
        return ans2


print(even_odd(num))
