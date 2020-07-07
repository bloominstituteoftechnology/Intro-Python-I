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
# printf("x is %d, ", x)
# printf("y is %.2f, ", y)
# printf('z is "%s"', z)
print('x is %d, y is %.2f, z is "%s"' % (x, y, z))
# Use the 'format' string method to print the same thing

print("\nx is {},".format(x), end=" ")
print("y is {:.2f},".format(y), end=" ")
print('z is "{}"'.format(z))

# Finally, print the same thing using an f-string
# f"x is {x}."
# f'y is {y:{4}.{3}}'
# f'z is "{z}"'
print(f'x is {x:d}, y is {y:.2f}, z is "{z:s}"');