# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE


def f1(a, b):
    """
    Add to variables and return the result
    """
    return(a + b)
print('f1 Sum two integers:')
print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE


def f2(*args):
    """
    thanks to the keywork *args(list of arguments) the function can add
    all the variables that are given
    """
    return sum(args)

print('\nf2 Python arbitrary arguments:')
print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?

"""
To use the *arg with a list we need
to unpack the list using *
"""
print('\n f2 modified funtion(*var) : ')
print(f2(*a))    # Should print 22

# Write a function f3 that accepts either one or two arguments.
# If one argument, it returns that value plus 1. If two arguments,
# it returns the sum of the arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE


def f3(a, b=None):
    """
    b = None means that the function admits 1 or 2 arguments
    """
    return(a + 1 if b is None else a + b)
print('\nf3 Python default arguments:')
print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
print('\nf4 Python keyword arguments:')


def f4(**kwargs):
    """
    Thanks to the keyword **kwargs allows handle
    named arguments and you can access them as a dictonary.
    """
    [print(f'key: {key}, value: {value}') for key, value in kwargs.items()]

# Should print
# key: a, value: 12
# key: b, value: 30
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
"""
To use the **kwargs with a dictionary we need
to unpack the dictionary using **
"""
print('\nf4 modified recieive a dictionary:')
f4(**d)
