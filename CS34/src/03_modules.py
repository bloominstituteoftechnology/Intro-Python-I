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


# Print out the OS platform you're using:
# YOUR CODE HERE
import platform
print(platform.version())
import os 
print(os.name)

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
print(sys.version_info)
import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

result1 = os.ctermid
print(result1)
# Print the current working directory (cwd):
# YOUR CODE HERE
result2 = os.getcwd
print(result2)
# Print out your machine's login name
# YOUR CODE HERE
result3 = os.getlogin
print(result3)