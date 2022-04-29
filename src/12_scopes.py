# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12
print(x)
def changeX():
    global x
    x = 99
    print(x)
changeX()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)

# This nested function has a similar problem.

def outer():
    y = 120
    print(y)
    def inner():
        nonlocal y
        y = 999
    inner()
    print(y)

#     # This prints 120. What do we have to change in inner() to get it to print
#     # 999? Google "python nested function scope".

outer()
