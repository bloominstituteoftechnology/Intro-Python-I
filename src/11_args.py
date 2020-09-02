# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(n1,n2):
    return n1 + n2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f02(*nums):
    my_sum = 0
    for x in nums:
        my_sum += x
    return my_sum

print(f02(1))                    # Should print 1
print(f02(1, 3))                 # Should print 4
print(f02(1, 4, -12))            # Should print -7
print(f02(7, 9, 1, 3, 4, 9, 0))  # Should print 33

# How do you have to modify the f2 call below to make this work?
def f2(my_list):
    the_sum = 0
    for i in my_list:
        the_sum += i
    return the_sum

a = [7, 6, 5, 4]
the_list = [1,2,3,4]

print(f2(the_list))
print(f2(a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f03(num):
    return num + 1

print(f03(8))   # Should print 9

def f3(num1, num2):
    return num1 + num2

print(f3(1, 2))  # Should print 3

# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(**words):
    # sentence = ''
    for letter in words:
        print('key: ' + letter + ', ' + 'value: ' + words[letter])
        # sentence += letter
    # return sentence

f4(foo = 'bar', baz = str(12))
f4(a= str(12), b=str(30))
f4(city="Berkeley", population=str(121240), founded="March 23, 1868")

# def f04(**words):
#     sentence = ''
#     for letter in words.values():
#         sentence += letter
#     return sentence

# print (f04(foo = 'bar', baz = str(12)))
# print (f4(a=12, b=30))

# Should print
# key: a, value: 12
# key: b, value: 30

# my_dict = {'a':12}
# other_dict = {'b':30}
# merged_dict = {**my_dict, **other_dict}

# print(merged_dict)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
# f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
def f04(**prop):
    for key in prop: 
        print(f'key: {key}' + ', value:' + str(prop[key]))

f04(**d)

def skip_count(n, start_from=0, skip_by=2):
    rv = []
    for i in range(n):
        rv.append(start_from + i * skip_by)
    return rv

print(skip_count(5, skip_by=3))