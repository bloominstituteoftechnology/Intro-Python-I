# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    # Its going to bring the x into the global scope as x in the function. 
    # It will now have access to x = 12 and we can change the value of x
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.
#  Both func need their own scope thats custom to their own function
def outer():
    y = 120

    def inner():
        # we use nonlocal to reach out into the parent scope and grab the variable we specify (y) if it finds it
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)

outer()
