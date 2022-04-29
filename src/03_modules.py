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
import sys
print(sys.argv)
print('This is the program:', sys.argv[0])
print('Argument List:', str(sys.argv))
print('Number of Arguments:', len(sys.argv)-1)
for arg in sys.argv:
    print('Here are the Arg list:', arg)


# Print out the OS platform you're using:
# YOUR CODE HERE
import platform
import os
print(os.name)
print(f'my OS platfom is: {platform.system()}')

# Print out the version of Python you're using:
# YOUR CODE HERE
import platform
print('Python Version:', platform.python_version())



import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('The friggin process ID: ',os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print('The working directory:', os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print('Here is my machine\'s login name:', os.getlogin())
