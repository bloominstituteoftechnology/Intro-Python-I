"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

import sys
def printf(format, *args):
    sys.stdout.write(format % args)


x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
printf("x is %d, y is %.2f, z is I like turtles!\n",   x , y )


# Use the 'format' string method to print the same thing
txt = "{nodecimal}"
txt2 = "{decimal: .2f}"
print("x is" + " " + txt.format(nodecimal = x) + "," + " " + "y is" + txt2.format(decimal = y)+ "," +" " + "z is" + " "+ z)

# Finally, print the same thing using an f-string
print(f'x is {x}, y is{txt2.format(decimal =y)}, z is {z}')