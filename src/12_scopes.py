# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    global x
    x = 99


change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
# use global keyword.
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # use nonlocal keyword to cause the variable to refer to the previously bound variable
    # in the closest enclosing scope.
    # Note: Google "python nested function scope".
    print(y)


outer()
