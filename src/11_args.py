# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

"""n a function declaration, * means “pack all remaining positional arguments into a tuple named <name>”, 
while ** is the same for keyword arguments (except it uses a dictionary, not a tuple).

In a function call, * means “unpack tuple or list named <name> to positional arguments at this position”, 
while ** is the same for keyword arguments.

 it is not necessary to write *args or **kwargs. 
Only the * (asterisk) is necessary.

*args and **kwargs are mostly used in function definitions. 
*args and **kwargs allow you to pass a variable number of arguments to a function. 
What variable means here is that you do not know beforehand how many arguments can be passed to your function by the user so in this case you use these two keywords. 
*args is used to send a non-keyworded variable length argument list to the function

**kwargs allows you to pass keyworded variable length of arguments to a function.
 You should use **kwargs if you want to handle named arguments in a function. 
 Here is an example to get you going with it:
"""





# YOUR CODE HERE
def f1(a, b):
    return a + b
print('F1', f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum. Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*args):
    return sum(args)


print('F2',f2(1))                    # Should print 1
print('F2',f2(1, 3))                 # Should print 4
print('F2',f2(1, 4, -12))            # Should print -7
print('F2',f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# What thing do you have to add to make this work?
print('F2', f2(*a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments. Google "python default arguments" for a hint.

# YOUR CODE HERE

def f3(*args):
     # args is returning a tuple, so need to convert to int, return an integer at 0th index so need plus 1  
    if len(args) == 1:
        return int(args[0]) + 1
    else:
        len(args) == 2
        return sum(args)
    
print('F3', f3(1, 2))  # Should print 3
print('F3', f3(8))     # Should print 9
print('F3', f3(20)) #working

# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Google "python keyword arguments".

# YOUR CODE HERE
#  **kwargs can accept multiple key value pair of arguments and will store them in dictionary 
# i.e. kwargs will be of dictionary type.
def f4(**kwargs):
    for key, value in kwargs.items():
        print(key, "is", value)
# Should print
# key: a, value: 12
# key: b, value: 30
print('F4', f4(a=12, b=30))

# # Should print
# # key: city, value: Berkeley
# # key: population, value: 121240
# # key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# # What thing do you have to add to make this work?
#need to let it know that it can take multiple args 
print('F4', f4(**d))



