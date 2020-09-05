"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import getpass
import sys
import argparse
import platform
import os

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

# Total arguments
n = len(sys.argv)
print("Total arguments passed: " + str(n))

# Arguments passed: 
print("\nName of python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# Print out the OS platform you're using:
# YOUR CODE HERE
print("My OS is", os.name)


# Print out the version of Python you're using:
# YOUR CODE HERE

print("My python Version is:", sys.version)
print("MY python version infi is:", sys.version_info)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print("This is my current process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE

print("My current working directory is", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE

username = os.getlogin()
username2 = getpass.getuser

print("My computers username is:", username)
print("MY computers username2 is", username2)