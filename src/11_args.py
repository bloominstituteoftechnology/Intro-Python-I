"""
https://www.programiz.com/python-programming/function-argument
Python Arbitrary Arguments

Sometimes, we do not know in advance the number of arguments that will be passed into a function. 
Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.

In the function definition, we use an asterisk (*) before the parameter name to denote this kind of argument.
https://www.geeksforgeeks.org/default-arguments-in-python/
"""


# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(x, y):
    return x+y

print("Part 1:")
print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*args):
    """
    This function sums all numbers
    passed through.
    """
    return sum(args)

print("Part 2:")
print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22
# add asterik


# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(x, y=1):
    return x+y

print("Part 3:")
print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(**kwargs):
    for i, j in kwargs.items():
     print(f"key:{i}, value:{j}")
#https://duckduckgo.com/?q=how+to+write+a+function+with+*kwargs+in+python&t=ffab&pn=1&iax=videos&ia=videos&iai=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dj0Mxlxedff8

# Should print
# key: a, value: 12
# key: b, value: 30
print("Part 4:")
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)

"""
ANSWERS:
Part 1:
3

Part 2:
1
4
-7
33
22 /n

Part 3:
3
9

Part 4:
key:a, value:12
key:b, value:30
key:city, value:Berkeley
key:population, value:121240
key:founded, value:March 23, 1868

key:monster, value:goblin
key:hp, value:3
"""