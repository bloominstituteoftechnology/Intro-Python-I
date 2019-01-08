# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    global x
    x = 99

changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
# ^^ add 'global x' inside the function
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
    # ^^ there are 3 ways
    ## 1) we could make y a list: y = [120], then in the function: y[0] = 999
    ## 2) we could add dot syntax: outer.y = 120, ind the function: outer.y = 999
    ## 3) we could tell the inner function to bring in a nonlocal variable with
        #the nonlocal keyword like I did above.
        
    print(y)

outer()