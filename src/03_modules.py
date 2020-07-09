"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:

# First will be printing out the number of arguments in the list
print(f"The number of arguments in the command line is {len(sys.argv)}\n")

# This is printing out each argument in the list (one per line)
for arg in sys.argv:
    print(arg)


# Print out the OS platform you're using:
print(f"\nThe platform that I am using is: {sys.platform}")

# getting the platform with the module called platform
import platform

print(f"\nThis is the platform info retrieved from the module platform:   {platform.platform()}")

# Print out the version of Python you're using:
print("\nThe version of python being used is: ", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f"\nThe current process ID is: {os.getpid()}")

# Print the current working directory (cwd):
print(f"\nThe current working directory is: {os.getcwd()}")

# Print out your machine's login name
print(f"\nMy machines login name is: {os.getlogin()}")
