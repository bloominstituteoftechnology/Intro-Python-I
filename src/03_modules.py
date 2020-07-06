"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""


# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
import os
import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))


# Print out the OS platform you're using:
# YOUR CODE HERE
print("This is the OS platform: ", os.name)


# Print out the version of Python you're using:
# YOUR CODE HERE
print("This is the version of Python I am using: ", sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("The current process ID is: ", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("This is the current working directory: ", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("This is my machine's login name: ", os.getlogin())
