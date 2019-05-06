"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for index, arg in enumerate(sys.argv):
    print(f'Arg number {index} is {arg}')

# Print out the OS platform you're using:
if sys.platform == 'darwin':
    print("The operating system is OSX.")

# Print out the version of Python you're using:
print(f'Python Version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'Current process ID: {os.getgid()}')

# Print the current working directory (cwd):
print(f'Current working directory: {os.getcwd()}')

# Print out your machine's login name
print(f'Current machine login name: {os.getlogin()}')
