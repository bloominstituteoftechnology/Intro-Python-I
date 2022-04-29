# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# # When you use a variable in a function, it's local in scope to the function.
# x = 12

# def change_x():
#     x = 99

# change_x()

# # This prints 12. What do we have to modify in change_x() to get it to print 99?
# print(x)


# # This nested function has a similar problem.

# def outer():
#     y = 120

#     def inner():
#         y = 999

#     inner()

#     # This prints 120. What do we have to change in inner() to get it to print
#     # 999?
#     # Note: Google "python nested function scope".
#     print(y)


# outer()

# 12
# https://github.com/LambdaSchool/Intro-Python-I/blob/master/src/12_scopes.py

# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# This nested function has a similar problem.

def outer():
    y = 120

    def inner(y):
        y = 999
        return y

    y = inner(y)

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    return print(y)


outer()