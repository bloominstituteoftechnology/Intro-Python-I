"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

"""
Import Statements:
"""
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
import os
import sys
print('Command Line Arguments:')
([(print(i)) for i in sys.argv], '\n')
print('\n')
# Print out the OS platform you're using:
print('+--------------------------+')
# YOUR CODE HERE
print('OS Platform:\n', sys.platform, '\n')

# Print out the version of Python you're using:
print('+--------------------------+')
# YOUR CODE HERE
print('Python Version:\n', sys.version, '\n')

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('+--------------------------+')
# YOUR CODE HERE
print('Current Process ID:\n', os.getpid(), '\n')

# Print the current working directory (cwd):
print('+--------------------------+')
# YOUR CODE HERE
print('Current Working Directory:\n', os.getcwd(), '\n')
# Print out your machine's login name
print('+--------------------------+')
# YOUR CODE HERE
print("Machine's Login Name:\n", os.getlogin(), '\n')
