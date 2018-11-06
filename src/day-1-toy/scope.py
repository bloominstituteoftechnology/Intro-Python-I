# Experiment with scope in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.


x = 12 # --> module-level/global by DEFAULT


# Use global keyword to read/write a global variable INSIDE A FUNCTION

def changeX():
   global x
   x = 99 # --> local/function level scope by DEFAULT   
   
changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y # --> this tells the inner function to look at the outer function's y variable
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()