# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE

def sum1(x, y):
    z = x + y
    print(z)

print(sum1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

def sum2(*args):
    sum = 0
    
    for num in args:
        sum = sum + num
        
    print("Sum:", sum)  

# YOUR CODE HERE

print(sum2(1))                    # Should print 1
print(sum2(1, 3))                 # Should print 4
print(sum2(1, 4, -12))            # Should print -7
print(sum2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a_list = [7, 6, 5, 4]

def sum3(*args):
    total = 0
    #for num in a_list:
    for num in args:
        total += num
    return total    
        
    print("Sum:", total)    

# How do you have to modify the f2 call below to make this work?
#unsure here
print(sum(a_list))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE

def sum4(integer1, integer2=1):
    result = integer1 + integer2
    return result

print(sum4(1, 2))  # Should print 3
print(sum4(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE

# Should print
def k_args(**kwargs):
    print(str(kwargs))
# key: a, value: 12
# key: b, value: 30
k_args(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
k_args(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
k_args(a=d)

