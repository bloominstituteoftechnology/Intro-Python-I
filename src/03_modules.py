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
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

for x in sys.argv:
    print("Argument: ", x)


# Print out the OS platform you're using:
# YOUR CODE HERE
os = sys.platform
print("OS platform: ", os)

# Print out the version of Python you're using:
# YOUR CODE HERE
version = sys.version
print("Python version: ", version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
process_id = os.getpid()
print("Current process ID: ", process_id)

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print("Current working directory: ", cwd)

# Print out your machine's login name
# YOUR CODE HERE
my_login = os.getlogin()
print("My machine login name: ", my_login)