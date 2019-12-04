# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables


"""
In Python, a variable declared outside of the function or in global scope is known as global variable. 
This means, global variable can be accessed inside or outside of the function.
"""
# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    global x
    x = 99
changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.
"""
Nonlocal variable are used in nested function whose local scope is not defined. This means, the variable can be neither in the local nor the global scope.

Let's see an example on how a global variable is created in Python.

We use nonlocal keyword to create nonlocal variable.


"""

def outer():
    y = 120
    def inner():
        nonlocal y  #have to create nonlocal scope 
        y = 999

    inner()
    

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()