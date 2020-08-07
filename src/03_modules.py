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
print(f"this is the name of the script:{sys.argv[0]}")
# Print out the OS platform you're using:
# YOUR CODE HERE

print(f'My OS is{" MacOSX" if sys.platform == "darwin" else "No Mac OSX"}')
# Print out the version of Python you're using:
# YOUR CODE HERE
print(f'My Current python version is: {sys.version}')

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f'Current process is {os.getpid()}')
# Print the current working directory (cwd):
# YOUR CODE HERE
print(f'Current directory I am in {os.getcwd()}')

# Print out your machine's login name
# YOUR CODE HERE
print(f'My login name is: {os.getlogin()}')
