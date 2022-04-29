# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE

# 11
# https://github.com/LambdaSchool/Intro-Python-I/blob/master/src/11_args.py
#
# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

def f1(x,y):
    return x+y

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

def f2(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33


a = [7, 6, 5, 4]
# How do you have to modify the f2 call below to make this work?

def f2(list_add):
    sum = 0
    for i in list_add:
        sum += i
    return sum

print(f2(a))    # Should print 22

# https://www.programiz.com/python-programming/function-argument
# "In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument. Here is an example."
# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# function to take 1 or 2 args: 
# if 1, print+1
# if 2, print sum
def f3(*input_numbers):
    # # for testing and inspection
    #print(len(input_numbers))

    # # for testing and inspection
    # print(input_numbers)

    # # for testing and inspection
    # print(type(input_numbers))
    
    if len(input_numbers) == 1:
        output = input_numbers[0]+1
    elif len(input_numbers) == 2:
        output = input_numbers[0]+input_numbers[1]
    
    return output


print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# def f4(**keywords):
#     # this iterates through the keys and values
#     # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops#3294899
#     for key, value in keywords.items():
#         print("key:", key)

def f4(**keywords):
    # this iterates through the keys and values
    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops#3294899
    for key, value in keywords.items():
        print("key:", key)
        print("value:", value)
    return

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
def f4(keywords):
    # this iterates through the keys and values
    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops#3294899
    for key, value in keywords.items():
        print("key:", key)
        print("value:", value)
    return

f4(d)