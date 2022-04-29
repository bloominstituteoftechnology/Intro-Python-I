# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x) # you have to state it as a global variable in line 8


# This nested function has a similar problem.

def outer():
    y = [120]
    print(y)

    def inner():
        y[0] = 999
    inner()
    print(y)

outer()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? # i guess add [square brackets around the value of y]
    # Note: Google "python nested function scope".
    