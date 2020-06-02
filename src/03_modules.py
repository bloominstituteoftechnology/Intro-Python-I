"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
"""
sys.argv is a list in Python, which contains
the command-line arguments passed to the script.
"""
# Print out the command line arguments in sys.argv, one per line:
for argument in sys.argv:
    print(argument)

# Print out the OS platform you're using:
print('\n Operaing system:')
print(sys.platform)


# Print out the version of Python you're using:
print('\n Python version:')
print(sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('\n Current Process ID:')
print(os.getpid())

# Print the current working directory (cwd):
print('\n Current working directory:')
print(os.getcwd())

# Print out your machine's login name
print('\n Login name:')
print(os.getlogin())
