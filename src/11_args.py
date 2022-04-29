# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE


def f1(num1, num2):
    return num1 + num2


print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
# def f2(*args):
#     for arg in args:
#         print(sum(args))


def f2(*args):
    # print(type(args))
    return sum(args)


print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22
# print(a)
#print(*a) #unpacks a's list // kind of like a spread operator

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE


def f3(num1, num2=1):
    return num1 + num2

# def f3(*args):
#     if len(args) == 1:
#         return args[0] + 1
#     elif len(args) == 2:
#         return sum(args)
#     else:
#         return print("invalid format")

# def f3(arg1, arg2=None):
#     if arg2 is None:
#         return arg1 + 1
#     else:
#         return arg1 + arg2


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
def f4(**kwargs):  # (**anything)
    for key, value in kwargs.items():
        # print("%s == %s" %(key, value))
        print(f"{key} == {value}")

# def f4(**my_dict):  # (**anything)
#     for key, value in my_dict.items():
#         # print("%s == %s" %(key, value))
#         print(f"{key} == {value}")

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
f4(**d)


def f5(a, b, *args, **kwargs): #(a, b, **kwargs, *args) error due to position
    print(a, b) 
    print(args) # tuple (3, 4, 5)
    print(kwargs) # dict {'x': 6, 'y': 7}

f5(1, 2, 3, 4, 5, x=6, y=7)

def f6(**kwds):
    print(kwds)

f6(a=1, b=2)

def f7(a, **kwds):
    print(a)
    print(kwds)

f7(a=1,b=2)