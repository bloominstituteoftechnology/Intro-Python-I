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
print(sys.argv)
# This is only returning the current file I am in.  What other arguments should it return?  What is the use of this?

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)
# returning darwin


# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
# returning 3.8.3 



import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
# returns 55210 but changes every time i run it

# Print the current working directory (cwd):
# YOUR CODE HERE
# print(os.getcwd())
# /Users/damonbogich/Documents/cs-projects/Intro-Python-I/src

# Print out your machine's login name
# YOUR CODE HERE
# print(os.getlogin())
# damonbogich
