# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.


def f1(a, b):
    return a + b
print(f1(1, 2))
print()

# Write a function f2 that takes any number
# of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"


def f2(*argv):
    a = 0
    for n in argv:
        a += n
    return a


a = [7, 6, 5, 4]
print(f2(1))
print()
print(f2(1, 3))
print()
print(f2(1, 4, -12))
print()
print(f2(7, 9, 1, 3, 4, 9, 0))
print()
print(f2(*a))
print()

# How do you have to modify the f2 call below to make this work?

# Write a function f3 that accepts either one or two arguments.
# If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.


def f3(*argv):
    a = 0
    for i in argv:
        a += i
    if a == argv[0]:
        return argv[0] + 1
    else:
        return a
print(f3(1, 2))
print()
print(f3(8))
print()

# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".


def f4(**kwargs):
    for key, value in kwargs.items():
        print(f'key: {key}, value: {value}')

# Should print
# key: a, value: 12
# key: b, value: 30

f4(a=12, b=30)
print()

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")
print()

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)
print()
