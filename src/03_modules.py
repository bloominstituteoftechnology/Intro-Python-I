"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
"""
sys.argv is a list in Python, which contains
the command-line arguments passed to the script.
"""
# YOUR CODE HERE
print('__SYS__')
print("sys.argv:\n")
"""
function that print all the elements of sys.argv
"""
for x in sys.argv:
    print(x)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("OS platform I'm using:\n", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Version of Python I'm using:\n", sys.version)

print('\n__OS__')
import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('Current process ID:\n',os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print('current working directory (cwd):\n',os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("My machine's login name: \n",os.getlogin())
