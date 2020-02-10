"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import fileinput
import os
import sys
import platform
from platform import python_version

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

# print(sys.argv)
# print(len(sys.argv))
for arg in sys.argv:
    print(arg)


# Print out the OS platform you're using:
# YOUR CODE HERE
print("Platform:", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("System Info: ", sys.version_info)
print("Python Version:", python_version())


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print("Current Process ID:", os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current Workign Directory:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE

print("Machine Login Name:", os.getlogin())
