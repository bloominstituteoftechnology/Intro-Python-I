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
for x in sys.argv:
    print(x)
# Print out the OS platform you're using:
# YOUR CODE HERE
print(os.name)

print(sys.platform)


# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
#'3.8.3 (default, Jul  2 2020, 11:26:31) \n[Clang 10.0.0 ]'

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
# 3296

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# '/Users/bsher/Documents/git/python/Intro-Python-I'
# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())
# 'bsher'
