# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def changeX():
    global x
    x = 99


changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
# In Python, global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.
# https://www.programiz.com/python-programming/global-keyword
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    # Have to use nonlocal keyword
    # The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
    print(y)


outer()
