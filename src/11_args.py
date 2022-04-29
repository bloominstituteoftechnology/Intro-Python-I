# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(int1, int2):
    return int1 + int2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*args):  
    total = 0
    for arg in args:  
        total = total + arg
    return total

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
# Function isn't designed to take a list. Could use a for loop or something explicit like below.
print(f2(a[0], a[1], a[2], a[3]))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(*args):
    my_args = []
    for arg in args:
        my_args.append(arg)
    if len(my_args) == 1:
        return my_args[0] + 1
    elif len(my_args) == 2:
        return my_args[0] + my_args[1]
    else:
        return "function accepts either one or two arguments"


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
def f4(**kwargs):
    names = []
    values = []
    for name in kwargs:
        names.append(name)
    for value in kwargs.values():
        values.append(value)

    for i in range(len(values)):
        print("key: {a}, value: {b}".format(a = names[i], b = values[i]))

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
# Agian, Explicit as function isn't designed to take an object but specific args.
f4(monster=d["monster"], hp=d["hp"])

