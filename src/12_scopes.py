# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

print(x)

def change_x():
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# Declare, within the function definition, that the global instance of x
# should be used.

def change_x():
    global x
    x = 99

print(change_x())


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        y = 999

    inner()

    print(y)


outer()


# This prints 120. What do we have to change in inner() to get it to print
# 999?

# Note: Google "python nested function scope".

# One way to handle it is to use, basically, function namespaces.


def outer():
    outer.y = 120

    def inner():
        outer.y = 999

    inner()

    print(outer.y)


outer()




