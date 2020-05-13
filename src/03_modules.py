"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for claw in sys.argv:
    print(claw)

# Print out the OS platform you're using:
print(sys.platform)

# Print out the version of Python you're using:
print(sys.version, "this is the version")

import os

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getppid(), "this is current process id")

# Print the current working directory (cwd):
print(os.getcwd(), "this is current process id")

# Print out your machine's login name
print(os.getlogin(), "this is machine login name")
