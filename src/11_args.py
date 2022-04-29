# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(x: int, y: int) -> int:
    return x + y

print(f1(1, 2))


# Python program to illustrate 
# *args for variable number of arguments 
# def myFun(*argv): 
# 	for arg in argv: 
# 		print (arg) 
	
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE

def f2(*argv) -> sum:
    sum = 0
    for arg in argv:
        sum += arg
        
    return sum

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22

# def greet(name, msg="Good morning!"):
#     """
#     This function greets to
#     the person with the
#     provided message.

#     If the message is not provided,
#     it defaults to "Good
#     morning!"
#     """

#     print("Hello", name + ', ' + msg)


# greet("Kate")
# greet("Bruce", "How do you do?")

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(x, y = 1) -> int:
    return x + y

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# def greet(*names):
#     """This function greets all
#     the person in the names tuple."""

#     # names is a tuple with arguments
#     for name in names:
#         print("Hello", name)


# greet("Monica", "Luke", "Steve", "John")

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))

# print(greet_me(name="yasoob"))


# YOUR CODE HERE
def f4(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}". format(key,value))

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

# e = {"hi": "bye"}

# How do you have to modify the f4 call below to make this work?
f4(**d)
# f4(**e)