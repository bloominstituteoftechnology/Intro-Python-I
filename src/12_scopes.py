# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    # Add this
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?

# make x global i.e the statement should flow as follows

print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        # Add the nonlocal keyword
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".

    # Add the nonlocal keyword
    print(y)


outer()
