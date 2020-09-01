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

for arg in sys.argv:
    print(f'Length of Command Line Arguments: {arg}')



#print(f'Length of Command Line Arguments: {len(sys.argv)}')
print(f'Command Line Argument: {sys.argv}')


'''
confused a bit on what this means.. ^^^
'''


# Print out the OS platform you're using:
# YOUR CODE HERE


import platform
print(f'Operating System: {platform.system()}')


# Print out the version of Python you're using:
# YOUR CODE HERE


print(f'Current Version of Python: {sys.version}')


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html


# Print the current process ID
# YOUR CODE HERE


import os
print(f'Current Process ID: {os.getpid()}')


# Print the current working directory (cwd):
# YOUR CODE HERE


print(f'Current Working Directory: {os.getcwd()}')


# Print out your machine's login name
# YOUR CODE HERE


print(f'Machine Login Name: {os.getlogin()}')


'''
run python src/03_modules.py in terminal
'''
