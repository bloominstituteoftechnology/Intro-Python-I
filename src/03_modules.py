"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import argparse
import platform
import os
import getpass
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

# Total Arguments:
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed:
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# Addition of numbers:
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
    print("\n\nResult:", Sum)

# for arg in sys.argv[1:]:
#     print(arg)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("My OS is:", os.name)

# Print out the version of Python you're using:
# YOUR CODE HERE

print("My Python Version is:", sys.version)
print("My Python Version Info is:", sys.version_info)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print("This is my Process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE

print("My Current working directory:", os.getcwd())


# Print out your machine's login name
# YOUR CODE HERE

username = os.getuid()
username2 = getpass.getuser()

print("My Computer Username2 is:", username2)
print("My Computer Username is:", username)
