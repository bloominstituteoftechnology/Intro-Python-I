"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print('Command line arguments: ')
print(sys.argv)
# Print out the OS platform you're using:
# YOUR CODE HERE

# Print out the version of Python you're using:
# YOUR CODE HERE
print('Version: ')
print(sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('Current process ID: ')
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print('Current working directory: ')
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("My machine's login name")
print(os.getlogin())
