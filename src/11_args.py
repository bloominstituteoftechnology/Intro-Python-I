# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.
def f1(rg1, rg2):
    return rg1 + rg2

print(f1(1, 2))
print("------")

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"
def f2(*arg):
    return sum(list(arg))

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33
print("------")


# How do you have to modify the f2 call below to make this work?
# NOTE: one possible solution to accomodate arguments as integers and lists
a = [7, 6, 5, 4]
def f2(*arg):
    wrk_lst = []
    # Iterate through the tuple of arguments
    for val in arg:
        # Handle an integer argument
        if type(val) is int:
            # Include integer val in summation
            wrk_lst.append(val)
            continue

        # Handle a list argurment
        if type(val) is list:
            # Include list elements if they are integers
            tmp_lst = [n for n in val if type(n) is int]
            wrk_lst.extend(tmp_lst)

        # Ignore all other value types

    # Sum integer values and return
    return sum(wrk_lst)

print(f2(a))    # Should print 22
print("------")

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.
def f3(num1:int, num2:int=None):
    if num2 == None:
        return num1 + 1

    return num1 + num2

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9
print("------")

# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".
def f4(**kwargs):
    # Iterate through the dict of argurments
    for k, v in kwargs.items():
        print(f'key: {k}, value: {v}')

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")
print("------")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
# Prefix the variable name with '**'
f4(**d)
