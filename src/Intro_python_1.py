''' Intro to Python I - Guided Project
    This document contains examples for CS Intro to Python, module 1. Examples
    focus on Python syntax & semantics plus the usage of lists, dicts, sets,
    and tuples.
'''
# How do we print something to the console?
print("Hello, world!")
# With f-strings?
# TODO
# Given an "out" string length 4, such as "<<>>", and a word, return a new 
# string where the word is in the middle of the out string, e.g. "<<word>>".
# (from CodingBat)
def make_out_word(out, word):
    # TODO
    pass
# print(make_out_word('<<>>', 'Yay')) # → '<<Yay>>'
# print(make_out_word('<<>>', 'WooHoo') # → '<<WooHoo>>'
# print(make_out_word('[[]]', 'word')) # → '[[word]]'
# Given an array of ints length 3, return the sum of all the elements.
# (from CodingBat)
def sum3(nums):
    # TODO
    pass
# print(sum3([1, 2, 3])) # → 6
# print(sum3([5, 11, 2]) # → 18
# print(sum3([7, 0, 0])) # → 7
# Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 7 (every 6 will be followed by at 
# least one 7). Return 0 for no numbers.
# (from CodingBat)
def sum67(nums):
    # TODO
    pass
# print(sum67([1, 2, 2])) # → 5
# print(sum67([1, 2, 2, 6, 99, 99, 7])) # → 5
# print(sum67([1, 1, 6, 7, 2])) # → 4
# Create a new list containing the squares of all values in `numbers`with a 
# list comprehension
numbers = [1, 2, 3, 4, 5]
print(numbers)
# TODO
# the equivalent of...
# TODO
# We can also use list comprehensions to filter!
# Create a new list containing only the even values of `numbers`
# TODO
# the equivalent of...
# TODO
# Can you use pieces of both of the above examples to...
# Create a new list containing only the names that start with `s` so that they 
# are properly capitalized (regardless of how the name originally appears) 
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
print(names)
# TODO

s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)
    
#do 1/2