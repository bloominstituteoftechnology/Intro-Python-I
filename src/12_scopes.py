# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    x = 99
    print("print 99:", x)
changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print("print 12:", x)


# This nested function has a similar problem.

def outer():
    y = 120
    print("print 120:", y)
    def inner():
        y = 999
        print("print 999:", y)
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()