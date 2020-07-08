# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x
    x = 99
change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.
def outer():
    
    y = 120

    def inner():
        global y
        y = 999
    inner()
    print(y)
outer()
