# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    x = 99

changeX()

# This prints 12. What do we have to modify below in changeY() to get it to print 99?
print(x)


y = 12

def changeY():
    global y # <== add this 'global' keyword
    y = 99

changeY()

# This should print 99.
print(y)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y # <== add this 'nonlocal' keyword
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()