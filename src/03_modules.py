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
for index, line in enumerate(sys.argv):
    print(f"sys.argv[{index}] = {line}")


# Print out the OS platform you're using:
# YOUR CODE HERE
print(f"sys.platform = {sys.platform}")
# Print out the version of Python you're using:
# YOUR CODE HERE
print(f"sys.version_info = {sys.version_info[3]}")

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f"os.getpgid(0) = {os.getpgid(0)}")
# Print the current working directory (cwd):
# YOUR CODE HERE
print(f"os.getcwdb(0) = {os.getcwd()}")
# Print out your machine's login name
# YOUR CODE HERE
print(f"os.getlogin() = {os.getlogin()}")
