"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("Command line arguments:")
for arg in sys.argv[1:]:  # First arg is filename
    print(arg)

# Print out the OS platform you're using:
print("\nOS Platform", sys.platform)

# Print out the version of Python you're using:
print("\nPython version:", sys.version)


import os

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("\nProcess ID:", os.getpid())

# Print the current working directory (cwd):
print("\nCWD:", os.getcwd())

# Print out your machine's login name
print("\nUser login name:", os.getlogin())
# Ugly method of getting the computer's name
print("Computer's network name:", os.uname()[1].split(".")[0])
