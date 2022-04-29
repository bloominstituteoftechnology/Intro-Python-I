"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print('Arguments:', str(sys.argv))


# Print out the OS platform you're using:
# YOUR CODE HERE
print('System', sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print('Python version', sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('Process Id is' , os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print('Current directory is', os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print('Login name is', os.getlogin())
