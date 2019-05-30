'''
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
'''

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

print(f'This is the name of the script: {sys.argv[0]}')
print(f'Number of arguments: {len(sys.argv)}')
print(f'The arguments are: {sys.argv}')

# Print out the OS platform you're using:
# YOUR CODE HERE

print(f'The OS platform you are using is: {sys.platform}')

# Print out the version of Python you're using:
# YOUR CODE HERE

major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]

print(f'The version of python you are using is: {major}.{minor}.{micro}')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print(f'The current process ID is: {os.getpid()}')

# Print the current working directory (cwd):
# YOUR CODE HERE

print(f'The current woring directory: {os.getcwd()}')

# Print out your machine's login name
# YOUR CODE HERE

print(f'The machine\'s login name is: {os.getlogin()}')

