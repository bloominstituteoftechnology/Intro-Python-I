"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
def python_printf():

    print("x : %2d, y : %3.2f, z : %s" %(x, y, z))

# Use the 'format' string method to print the same thing

def python_string_format():

    print("x : {0}, y : {1:3.2f}, z : {2}".format(x, y, z))

# Finally, print the same thing using an f-string
def python_f_string():

    print(f"x : {x}, y : {y:.2f}, z : {z}")

if __name__ == "__main__":
    python_printf()
    python_string_format()
    python_f_string()