"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
import platform
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("=== sys.argv ===")
print(sys.argv[0])
print('================\n')

# Print out the OS platform you're using:
# YOUR CODE HERE
print("=== OS Platform ===")
print(f" OS name: {platform.platform()}")
print('===================\n')

# Print out the version of Python you're using:
# YOUR CODE HERE
print("=== Python Version ===")
print(f" Python version # : {platform.python_version()}")
print("======================\n")


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("=== Process ID ===")
print(f" Current Process ID : {os.getpid()}")
print("==================\n")

# Print the current working directory (cwd):
# YOUR CODE HERE
print("=== Current Working Dir ===")
print(f" Dir : {os.getcwd()}")
print("===========================\n")

# Print out your machine's login name
# YOUR CODE HERE
print("=== Login Name ===")
print(f" Dir : {os.getlogin()}")
print("==================\n")
