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
print("Number of arguments:", len(sys.argv))
print("Script name: ", sys.argv[0])

for arg in sys.argv:
    print("Argument: ", str(arg))
# Print out the OS platform you're using:
# YOUR CODE HERE
print("The OS platform: ", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python version: ", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
pid = os.getpid()
print("Process ID: ", pid)

# Print the current working directory (cwd):
# YOUR CODE HERE
path = os.getcwd()
print("Current path: ", path)

# Print out your machine's login name
# YOUR CODE HERE
name = os.getlogin()
print("Machines login name: ", name)
