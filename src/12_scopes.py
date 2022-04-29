# Experiment with scopes in Python.
# Good reading:
# https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    x = 99
    return x


# This prints 12. What do we have to modify in change_x()
# to get it to print 99?
"""
Change_x() is creating a copy of x and then applying a operation
for that reason we cannot see the change in the global variable x
If we want to reflect the chnage in x we have to pass the result
of the function into the variable
"""
x = change_x()

print('First problem:')
print(x)

# This nested function has a similar problem.


def outer():
    y = 120

    def inner():
        y = 999
        return y
    y = inner()
    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    """
    inner() is creating a copy of y and then applying a operation
    for that reason we cannot see the change in the variable 'y'
    If we want to reflect the change in 'y' we have to pass the result
    of the function into the variable
    y = inner()
    """
    print(y)

print('Second problem:')
outer()
