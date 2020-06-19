"""
print("Hello,world!")
"""

# loops (for/while/other)---> 
"""
for i in range(5):
    print(i)
"""

"""
for i in range (5, 10):
    print(i)
"""

"""
for i in range (5, 10, 2):
    print(i)
"""

"""                  # ----> u can use these quotation to hide the code from running on python 
x = 5
while x <10:
    print(x)
    x += 1

if x == 10:
    print("x is 10")

if x == 9 or x == 10: 
    print("x is 9 or 10")
"""                           # ---------->  every set of data has a type attached to it 

# conditionals
# arrays ("lists" in python)
"""
a = [1,2,3]
print(a[1])
print(len(a))
"""
"""
a = [44] * 10
a[0] = 999
a[len(a)-1] = 5555 ------> insert number on the end
a[-1] -----> makes last number in list
a[:4] -----> slices of list / slices makes new list
a[2:4]
a[:]
a[-3:] -----> last element on the list 
print(a)
"""
# input 
# tuples
# changing types
# lists
# dictionaries
"""
d = {

    "x": 12,
    "y": 38,
    "z": "hello",
}
print(d['y'])
"""
# math
# for-in
# modules
# sets
# classes
# inheritance
# higher order components
# curring
# functions 

def foo(a, b, baz):
    print(f"this is function foo! and a is {a}")
    
foo(1.23, 99, baz="hi")
